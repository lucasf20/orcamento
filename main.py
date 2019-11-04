from composicao import *
from sinapiInsumosDesonerado import *
from getDataRevit import *
import pandas as pd 
import numpy as np

ins = Insumos()

rvt = RevitData()

comp = ComposicaoAnalitica(r'C:\Users\lucas\Desktop\dynamo_sinapi\orcamento-master\SINAPI_Custo_Ref_Composicoes_Analitico_MA_201908_Desonerado.xls')

codcomp = rvt.codigos

insumosPorComposicao = [comp.achaInsumosPorComposicao(cod) for cod in codcomp]

quantidade = rvt.qntidades

def insumos(composicao):
    codigo = 0
    descricao = 0
    unidade = ''
    precoUnitario = 0
    indice = 0 
    i = 0
    linha = []
    
    for item in composicao:
        if indice == 0:
            linha.append([item,'-',comp.descricao(item),'',''])
        else:
            if type(item) == list:
                linha += (insumos(item))
            else:
                codigo = item
                descricao = ins.descricao(codigo)
                unidade = ins.unidadeMedida(codigo)
                precoUnitario = ins.precoUnitario(codigo)
                linha.append(['',codigo,descricao,unidade,precoUnitario])
                i += 1
        indice += 1
    return linha

def custototal():
    a = []
    for i in range(len(quantidade)):
        a += comp.custoTotal(codcomp[i],quantidade[i]) 
    return a

def insum():
    dados = []
    for i in insumosPorComposicao:
        dados += insumos(i)
        dados.append(['     ','-','     ','     ','     ','     '])
    return dados

writer = pd.ExcelWriter('teste.xlsx', engine='xlsxwriter')

ct1 = custototal()

ct = [c[0] for c in ct1]

qnts = [c[1] for c in ct1]

da = insum()

i = 0

for d in da:
    if d[1] != '-':
        d.append("{0:.2f}".format(qnts[i])) 
        d.append("{0:.2f}".format(ct[i])) 
        i+= 1
    else:
        if len(d) < 6:
            d.append(" ")
        d.append(" ")


data = pd.DataFrame(np.array(da),columns = ['CODIGO COMPOSICAO','CODIGO INSUMO' ,'DESCRICAO','UNIDADE','PRECO UNITARIO','QUANTIDADE','CUSTO TOTAL'])

data.to_excel(writer, sheet_name = 'orcamento 1')

writer.save()

print("Planilha exportada com sucesso")


