

Lista = [1,2,3,4]

## consigo adicionar mais numeros a lista a partir do comando

Lista +=[7,8,9]

print(Lista)


#posso somar elementos da lista
## aqui estou somando o 1 mais o 3
soma = Lista[0]+Lista[2]
print(soma)

##consigo mudar os elementoa
Lista[1]=5.5
print(Lista)

#consigo tamb´me percorrer elementos de uma lista
#slance
print(Lista[0:3])

#Consigo mostrar os elemento e também soma-los
print(Lista[0:3:2])

## conssigo inverter a lista

print(Lista[::-1])


##consigo colocar uma lista dentro da outra

lista= [1,2,3,4,[5,4,8,9]]
print(lista)

## para mostrar os elementos da lista

lista[4][2]
print(lista)
