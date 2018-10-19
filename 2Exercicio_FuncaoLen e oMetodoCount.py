
import random

ArmazenaDados=[]

for i in range(100):
    Valores_Dado = random.randint(1,6)
    ArmazenaDados.append( Valores_Dado)
for i in range(1,7):
    print("A face %i aparecer %i vezes."%(i, ArmazenaDados.count(i)))
      
