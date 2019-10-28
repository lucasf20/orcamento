from composicao import *
from sinapiInsumosDesonerado import *
import pandas as pd 
import numpy as np
import multiprocessing

ins = Insumos()

comp = ComposicaoAnalitica('SINAPI_Custo_Ref_Composicoes_Analitico_MA_201908_Desonerado.xls')

codcomp = [100036,100037, 5684, 5841, 72137, '73767/2', '73856/8', 83361]

insumosPorComposicao = [comp.achaInsumosPorComposicao(cod) for cod in codcomp]

quantidade = [1,53,31,4,6,8,4,2]

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

def processo2(con):
    a = []
    for i in range(len(quantidade)):
        a += comp.custoTotal(codcomp[i],quantidade[i]) 
    con.put(a)

def processo3(con):
    dados = []
    for i in insumosPorComposicao:
        dados += insumos(i)
        dados.append(['     ','-','     ','     ','     ','     '])
    con.put(dados)


q1 = multiprocessing.Queue()

q2 = multiprocessing.Queue()

p1 = multiprocessing.Process(target=processo2,args=(q1,))

p2 = multiprocessing.Process(target=processo3,args=(q2,))

p1.start()
p2.start()

#maodeobra = [comp.maoDeObraComposicao(i) for i in codcomp]

writer = pd.ExcelWriter('teste.xlsx', engine='xlsxwriter')

ct = q1.get()

i = 0
da = q2.get()

for d in da:
    if d[1] != '-':
        d.append("{0:.2f}".format(ct[i])) 
        i+= 1
    else:
        if len(d) < 6:
            d.append(" ")


data = pd.DataFrame(np.array(da),columns = ['CODIGO COMPOSICAO','CODIGO INSUMO' ,'DESCRICAO','UNIDADE','PRECO UNITARIO','CUSTO TOTAL'])

data.to_excel(writer, sheet_name = 'orcamento 1')

writer.save()

print("Planilha exportada com sucesso")


