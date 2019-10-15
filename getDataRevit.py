import pandas as pd

def openCsv():
    csv = pd.read_csv("inf.csv")
    i = 0
    inf = []
    while i<len(csv.values):
        aux = csv.values[i][0]
        inf.append(aux.split())
        i += 1
    return inf

def getCodigo(i):
    inf = openCsv()
    try:
        codigo = int(inf[i][0])
    except:
        print("Codigo invalido na linha %i"%(i+1))
    return codigo

def getQuantidade(i):
    inf = openCsv()
    try:
        quatidade = float(inf[i][1])
    except:
        print("quantidade invalida na linha %i"%(i+1))
    return quatidade

def getAllCodigos():
    i = 0
    cod = []
    while i < len(openCsv()):
        cod.append(getCodigo(i))
        i+=1
    return cod

def getAllQuantidades():
    i = 0
    qnt = []
    while i < len(openCsv()):
        qnt.append(getQuantidade(i))
        i+=1
    return qnt
