

Lista=[]
NumerosMaior10=[]
print("
print("digite -1 para parar\n\n")
e= int(input("Digite um numero:  "))
while e != -1 :
    Lista.append(e)
    e= int(input("Digite um numero:  "))

for i in range(len(Lista)):
    if Lista[i]> 10 :
            NumerosMaior10.append(Lista[i])
print(NumerosMaior10)
