"""Dizemos que número natural é triangular se ele é produto de três números naturais consecutivos.

Exemplo:120 é triangulo,pois 4.5.6 ==120.
dado um inteiro não negativo n, verificar se n é triangular.

"""
num = int(input("Dite um numero: "))
i,j,k = 1,2,3

while i * j * k < num :
    i+=1
    j+=1
    k+=1
    
if i*j*k != num:
    
    print(num,"Não é triangular")
else:
    print(num,"é triangular")
