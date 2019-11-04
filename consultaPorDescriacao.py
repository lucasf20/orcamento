from sinapiInsumosDesonerado import *

plan = Procura()
descricao = input("Descricao:   ")
results = plan.consultaPorDescricao(descricao)
print(results[0])
print("\n" + str(results[1]) + " resutados encontrados")