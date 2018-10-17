#o ciclo for é um clico que percorre uma determinada sequencia a partir do uso de uma variavel qualquer
#range recebe três valores, exemplo range(começo,fim,valor de incremento) lembrando que o fim é diferente do numero digitado é sempre um numero abaixo
n = 10
for cont in range(n):
    print(cont)

    print("  ")

""" 2 é onde ele inicia e 6 é onde ele termina"""
for cont in range(2,6):
    
    print(cont)

    
""" o ultimo 2 é uma soma ele soma 2 ao cont"""
for cont in range(2,12,2):
    
    print(cont)

"""posso fazer de uma forma decrescente também"""
for cont in range(10,0,-2):
    
    print(cont)
