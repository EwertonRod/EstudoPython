""" imprim a soma do entre o  nuemro digitado
por exemplo: se digitado: 5 = 1+2+4+5 = 15"""

n = int(input("Digite o primeiro numero"))
i=0
result = 0
while i < n and n > 0:
    i = i + 1       
    result = i + result
print( result )
