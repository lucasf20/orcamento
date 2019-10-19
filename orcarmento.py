from getDataRevit import *
from sinapiInsumosDesonerado import *
import pandas as pd
import os


plan = Procura()
rev = RevitData()

codigos = rev.getAllCodigos()
quantidades =  rev.getAllQuantidades()
precosUnitarios = []
precosTotais = []
unidades = []
descricoes = []
writer = pd.ExcelWriter('orcamento.xlsx', engine='xlsxwriter')

i = 0
total = 0 

while(i < len(codigos)):
    precosUnitarios.append(plan.precoUnitario(codigos[i]))
    precosTotais.append(float("{0:.2f}".format(precosUnitarios[i]*quantidades[i])))
    unidades.append(plan.consultaPorCodigo(codigos[i])[2])
    descricoes.append(plan.consultaPorCodigo(codigos[i])[1])
    total += precosTotais[i]
    i += 1

codigos.append(" ")
descricoes.append(" ")
unidades.append(" ")
quantidades.append(" ")
precosUnitarios.append("Valor total:")
precosTotais.append(total)

data = {'Codigo':codigos,'Descricao':descricoes,'Unidade':unidades,'Quantidade':quantidades,'Preco Unitario':precosUnitarios,'Preco total':precosTotais}

df = pd.DataFrame(data)

try:
    df.to_excel(writer,sheet_name='orcamento1')
    writer.save()
    os.system("clear")
    print("Planilha criada com sucesso!!!\n")
except:
    print("Falha ao exportar a planilha\n")
