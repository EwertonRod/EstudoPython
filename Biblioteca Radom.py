import random

#random.randrange(start,stop,step)
# escolhes numeros aleatorios

for i in range(10):
    x = random.randrange(1,7)
    print(x)

for i in range(10):
    x = random.choice([1,2,3,4,5,6,7])
    print(x)

for i in range(10):
    x = random.choice([1,2,3,4,5,6,7])
    print(x)

for i in range(10):
    x = random.uniform(1,7)
    print(x)

