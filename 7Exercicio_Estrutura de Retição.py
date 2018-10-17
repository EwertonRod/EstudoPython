"""Programano ano em que a pessoa completa tal idade

"""

num_person= int(input("Digite o numero de pessoas: "))


cont =0
numeroP=1;
while cont < num_person :
    print("{} pessoa".format(numeroP))
    numeroP=numeroP+1
    dia = int(input("Digite o dia do seu nascimento: "))
    mes = int(input("Digite o mês do seu nascimento: "))
    ano = int(input("Digite o ano do seu nascimento: "))
    idade = int(input("Digite a idade que quer fazer: "))
    anoQueCompleta = idade + ano

    print("{}/{}/{} você completa {}\n".format(dia,mes,anoQueCompleta,idade))
    
    cont+=1
