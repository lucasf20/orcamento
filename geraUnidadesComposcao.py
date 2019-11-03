from composicao import *
import pandas as pd 

plan =  ComposicaoAnalitica('SINAPI_Custo_Ref_Composicoes_Analitico_MA_201908_Desonerado.xls')
cod = []
uni = []
nLine = 1
for linha in plan.sheet[0].values:
    if nLine > 7:
        if linha[11] != "COMPOSICAO" and linha[11] != "INSUMO":
            uni.append(linha[8])
            cod.append(linha[6])
    nLine += 1

writer = pd.ExcelWriter('unidades.xlsx', engine='xlsxwriter')

dados = {'Codigos':cod,'Unidades':uni}

data = pd.DataFrame(data = dados)

data.to_excel(writer, sheet_name = 'Unidades')

writer.save()

