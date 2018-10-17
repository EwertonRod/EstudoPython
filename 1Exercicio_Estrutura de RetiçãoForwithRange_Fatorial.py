#o ciclo for é um clico que percorre uma determinada sequencia a partir do uso de uma variavel qualquer
#range recebe três valores, exemplo range(começo,fim,valor de incremento) lembrando que o fim é diferente do numero digitado é sempre um numero abaixo


numero= int(input("Digite um número: "))
fatorial = 1
for cont in range(1,numero+1):
    
    fatorial =fatorial*cont
  
    
print("o Fatorial de {}!={}".format(numero,fatorial))
