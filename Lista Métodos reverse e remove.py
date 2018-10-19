
n = int(input("Digite o numero de elementos da lista: "))
lista= []
aux = []


for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1,n)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux :
    aparicao = lista.count(ele)
    for i in range(aparicao-1):
        lista.remove(ele)
print( lista)








#usando slice para inverte a ordem lida
"""
idades_invertida= idades[::-1]

altura_invertida= alturas[::-1]

"""
