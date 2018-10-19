lista1 = [1,2,3,5,8,9,6]

## 
lista = []
cont= 0
num = int(input("Digite um número da serquência:"))
while num != -1 :
    lista.append(num)
    num = int(input("Digite um número da serquência:"))


elemento = int(input("Digite o elemento a ser procurado:"))

print("o elemento aparece %i vezeses"%lista.count(elemento))




"""
for i in range ( len(lista)):

    if elelmento == lista[i]:
        cont+=1
print("o elemento aparece %i vezeses"%cont)
"""
