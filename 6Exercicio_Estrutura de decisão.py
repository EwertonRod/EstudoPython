
print("\t\tLe 3 numeros e devolve o maior e o menor")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1>num2 and num1>num3  and num2<num3:
    print("O maior é o {}".format(num1))
    print("O menor é o {}".format(num2))
    
elif num1>num2 and num1>num3  and num3<num2:
    print("O maior é o {}".format(num1))
    print("O menor é o {}".format(num3))


elif num2>num1 and num2>num3 and num1<num3 :
          print("O  maior é o {}".format(num2))
          print("O menor é o {}".format(num1))
          

elif num2>num1 and num2>num3 and num3<num1 :
          print("O  maior é o {}".format(num2))
          print("O menor é o {}".format(num3))

          
elif num3>num1 and num3>num2 and num1<num2 :
        print("O  maior é o {}".format(num3))
        print("O menor é o {}".format(num1))
                
elif num3>num1 and num3>num2 and num2<num1 :
        print("O  maior é o {}".format(num3))
        print("O menor é o {}".format(num2))
