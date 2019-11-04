import pandas as pd

class RevitData:
    codigos = []
    qntidades = []
    unidades = []
    def __init__(self):
        xls = pd.ExcelFile (r'C:\Users\lucas\Documents\inf.xlsx')
        table = xls.parse(0)
        for linha in table.values:
            self.codigos.append(linha[0])
            self.qntidades.append(linha[1])
            self.unidades.append(linha[2])   