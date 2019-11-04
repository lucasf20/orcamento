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
        for linha in self.sheet[0].values:
            if codigo == linha[6]:
                desc = linha[7]
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
        codInsumos = [codComposicao]
        for linha in self.sheet[0].values:
            if linha[6] == codComposicao:
                if linha[11] == "COMPOSICAO":
                    codInsumos.append(self.achaInsumosPorComposicao(linha[12]))
                if linha[11] == "INSUMO":
                    codInsumos.append(linha[12])
        return codInsumos
    
    def maoDeObraComposicao(self, codComposicao):
        codComposicao = str(codComposicao)
        rst = 0
        for linha in self.sheet[0].values:
            if linha[6] == codComposicao:
                if linha[11] != 'COMPOSICAO' and linha[11] != 'INSUMO':
                    rst = str(linha[19])
                    aux = ''
                    for n in rst:
                        if n != ',' and n != '.':
                            aux += n
                        else:
                            if n == ',':
                                aux += '.'
                    rst = float(aux) 
        return rst

    def custoTotal(self,codComposicao, qntdade):
        codComposicao = str(codComposicao)
        rst = []
        for linha in self.sheet[0].values:
            if linha[6] == codComposicao:
                if linha[11] == 'INSUMO':
                    aux = ''
                    aux2 =''
                    for n in linha[18]:
                        if n != '.' and n != ',':
                            aux += n
                        else:
                            if n == ',':
                                aux += '.'
                    for n in linha[16]:
                        if n != '.' and n != ',':
                            aux2 += n
                        else:
                            if n == ',':
                                aux2 += '.'
                    rst.append([float(aux) * qntdade, float(aux2)*qntdade])
                if linha[11] == 'COMPOSICAO':
                    aux = ''
                    for n in linha[16]:
                        if n != '.' and n != ',':
                            aux += n
                        else:
                            if n == ',':
                                aux += '.'
                    rst += self.custoTotal(linha[12],float(aux))
        return rst