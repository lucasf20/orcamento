import pandas as pd

def openXls():
    xls = pd.ExcelFile("SINAPI_Preco_Ref_Insumos_MA_201908_Desonerado.xls")
    sheet = xls.parse(0)
    return sheet

def precoUnitario(codigo):
    try:
        valor = consultaPorCodigo(codigo)[4]
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

def descricao(codigo):
    valor = consultaPorCodigo(codigo)[1]
    return valor 

def unidadeMedida(codigo):
    return consultaPorCodigo(codigo)[2]

def consultaPorCodigo(codigo):
    result = []
    i = 0
    sheet = openXls()
    while i<len(sheet.values):
        if str(sheet.values[i][0]) == str(codigo):
            result = sheet.values[i]
            break
        i += 1
    return result

def imprimeResultado(codigo):
    r = consultaPorCodigo(codigo)
    if len(r) == 5:
        print("Codigo: " + str(r[0]))
        print("Descricao: " + str(r[1]))
        print("Unidade de Medida: " + str(r[2]))
        print("Origem do preco: " + str(r[3]))
        print("Preco mediano: R$ " + str(r[4]))
    else:
        print("Codigo incorreto")

