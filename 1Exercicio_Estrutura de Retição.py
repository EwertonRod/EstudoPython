""" ciclo while"""


base = int(input("Digite a base"))
expoente = int(input("Digite o expoente"))
cont =0
result=1
while cont < expoente :
    result = base * result
    cont=cont+1
    print(result)
if expoente == 0:
    print(result)
