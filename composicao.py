import re

import pandas as pd


class ComposicaoAnalitica:
    p = ""
    sheet = []
    codigos = []
    
    def __init__(self,path):
        self.p = path
        self.abrir()
    
    def abrir(self):
        xls = pd.ExcelFile(self.p)
        self.sheet.append(xls.parse(0))
        self.sheet.append(xls.parse(1))
    
    def todosCodigos(self):
        self.abrir()
        planilha = self.sheet[1].values
        codigos = []
        for linha in planilha:
            codigos.append(linha[0])
        return codigos
    
    def descricao(self, codigo):
        desc = ""
        codigo = str(codigo)
        for linha in self.sheet[1].values:
            if codigo == linha[0]:
                desc = linha[1]
                break
        return desc
    
    def achaCodigoPorDescricao(self, descri):
        pattern = ".*(" + descri.upper() + ").*"
        descs = [str(linha[1]) for linha in self.sheet[1].values]
        matches = []
        for i in range(len(descs)):
            if re.match(pattern,descs[i]):
                matches.append(self.sheet[1].values[i][0])
        return matches
    
    def achaInsumosPorComposicao(self,codComposicao):
        codComposicao = str(codComposicao)
        codInsumos = []
        for linha in self.sheet[0].values:
            if linha[6] == codComposicao:
                if linha[11] == "COMPOSICAO":
                    codInsumos.append(self.achaInsumosPorComposicao(linha[12]))
                if linha[11] == "INSUMO":
                    codInsumos.append(linha[12])
        return codInsumos

        
c = ComposicaoAnalitica('SINAPI_Custo_Ref_Composicoes_Analitico_MA_201908_Desonerado.xls')

print(c.achaInsumosPorComposicao(97141))
