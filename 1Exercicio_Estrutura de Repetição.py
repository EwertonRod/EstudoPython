"""
Faça um programa que peça dois números e imprima o maior deles.
"""
print("\t\tImprime o Maior numero\n")
num1 = int (input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maiornum1 = num1 > num2

if maiornum1 == True :
    print("o numero {} e maior".format(num1))
          
else:
            print("o numero {} e maior".format(num2))

                
