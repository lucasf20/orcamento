import pandas as pd
import re

class Insumos:
    def openXls(self):
        xls = pd.ExcelFile("SINAPI_Preco_Ref_Insumos_MA_201908_Desonerado.xls")
        sheet = xls.parse(0)
        return sheet

    def precoUnitario(self,codigo):
        try:
            valor = self.consultaPorCodigo(codigo)[4]
            rst = ""
            for n in valor:
                if n != "." and n != ",":
                    rst += n
                else:
                    if n == ".":
                        rst += ""
                    if n == ",":
                        rst += "."
            return float(rst)
        except:
            print("O codigo " + str(codigo) + " nao existe")
            exit(0)
            return "erro"

    def descricao(self,codigo):
        valor = self.consultaPorCodigo(codigo)[1]
        return valor 

    def unidadeMedida(self,codigo):
        return self.consultaPorCodigo(codigo)[2]

    def consultaPorCodigo(self,codigo):
        result = []
        i = 0
        sheet = self.openXls()
        while i<len(sheet.values):
            if str(sheet.values[i][0]) == str(codigo):
                result = sheet.values[i]
                break
            i += 1
        return result

    def imprimeResultado(self,codigo):
        r = self.consultaPorCodigo(codigo)
        if len(r) == 5:
            print("Codigo: " + str(r[0]))
            print("Descricao: " + str(r[1]))
            print("Unidade de Medida: " + str(r[2]))
            print("Origem do preco: " + str(r[3]))
            print("Preco mediano: R$ " + str(r[4]))
        else:
            print("Codigo incorreto")

    def consultaPorDescricao(self,descri):
        pattern = ".*(" + str(descri).upper() + ").*"
        planilha = self.openXls().values
        des_material = [str(linha[1]) for linha in planilha]
        codigo = [linha[0] for linha in planilha]
        matches = []
        i = 0
        n = 0
        while i < len(des_material):
            if re.match(pattern,des_material[i]):
                matches.append(planilha[i])
                n += 1
            i += 1
        return [matches,n]

