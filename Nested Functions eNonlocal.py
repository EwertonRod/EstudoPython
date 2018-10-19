#Nested functions é colocar uma função dentro de outra função


#Lista de comida

def lista():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista,start # diz que existe uma variavel definida dentro da função lista
        lista.append(item)
        start +=1
        print(item,start)
    return incrementa

compras1 = lista()
compras1('presunto')
compras1('Queijos')
compras1('pão')



"""
x =100
def f1():
    global x
    def f2():
        print(x)
    f2()

print(f1())



def exp (n):
    x =2
    n = 5
    def eleva():
       print( x**n)
   # return eleva

"""
