#o ciclo for é um clico que percorre uma determinada sequencia a partir do uso de uma variavel qualquer
#range recebe três valores, exemplo range(começo,fim,valor de incremento) lembrando que o fim é diferente do numero digitado é sempre um numero abaixo

"""tabuada"""
a=1
numeroInicio = int(input("Digite o numero de inicio da tabuada: "))
numeroFinal = int(input("Digite o ultimo numero da tabuada: "))
for i in  range(numeroInicio,numeroFinal+1):
    print("Para {}".format(a))
    for j in range(numeroInicio,numeroFinal+1):
     
         mult = i*j
        
         
         print("{} x {} = {}".format(i,j,mult))
         print("  ")
    a=a+1;
