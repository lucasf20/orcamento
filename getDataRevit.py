import pandas as pd

class RevitData():
    def openCsv(self):
        csv = pd.read_csv("inf.csv")
        i = 0
        inf = []
        while i<len(csv.values):
            aux = csv.values[i][0]
            inf.append(aux.split())
            i += 1
        return inf

    def getCodigo(self,i):
        inf = self.openCsv()
        try:
            codigo = int(inf[i][0])
        except:
            print("Codigo invalido na linha %i"%(i+1))
        return codigo

    def getQuantidade(self,i):
        inf = self.openCsv()
        try:
            quatidade = float(inf[i][1])
        except:
            print("quantidade invalida na linha %i"%(i+1))
        return quatidade

    def getAllCodigos(self):
        i = 0
        cod = []
        while i < len(self.openCsv()):
            cod.append(self.getCodigo(i))
            i+=1
        return cod

    def getAllQuantidades(self):
        i = 0
        qnt = []
        while i < len(self.openCsv()):
            qnt.append(self.getQuantidade(i))
            i+=1
        return qnt
