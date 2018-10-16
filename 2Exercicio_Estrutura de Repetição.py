"""
Faça um programa para uma loja de tintas.

o programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
considere que a cobertura de tinta é de 1 litro para cada 3 metros quadrados e que atinta
é vendida em latas de 18 litros, que custam r$ 80,00.

informe ao usuário a quantidade de latas de tintas a serem compradas e o preço total.
"""
print("\t\tloja de tintas\n")
area= int (input("Tamanho em metros quadrados da area:  "))

litros = area//3

if area%3 > 0 :
    litros = litros+ 1
    

          
latas = litros//18
if litros %18>0:
    latas = latas+ 1



    preco= latas*80
    print("o gasto será {}".format(preco))  
    print("a quanidade de latas {}".format(latas))   
   
