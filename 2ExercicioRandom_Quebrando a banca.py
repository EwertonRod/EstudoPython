import random


############
TrocadePorta=0
escolha2= 0
print("Olá,bem-vindo ao nosso programa! vamos ver se você vai ganhar um carro ou não!\n\n")
escolha = int(input("Escolha uma porta de 1 a 3: "))
Abrir_porta_Aleatoria = random.randint(1,3)
###########Primeiro bloco IF ####################################################
if escolha != Abrir_porta_Aleatoria:
    print("Você escolheu a porta {} mas eu lhe informo que a pota {} há um bode".format(escolha,Abrir_porta_Aleatoria) )
    TrocadePorta = int(input("Deseja Trocar de porta (1-sim/0-não): " ))
################ Segundo Bloco IF ################################################
if TrocadePorta  == 1:
    escolha2 = int(input("Escolha a porta: "))
    TrocadePorta = int(input("Deseja Trocar de porta (1-sim/0-não): " ))
################ Terceiro Bloco IF ###################################################    
    if escolha2 != escolha   and escolha2 !=  Abrir_porta_Aleatoria :

                 print("Ganhou um Carro!")
################ Fecha Terceiro Bloco IF ##############################################  
    else :
        print("Você perdeu ")
        
################ Fecha o primeiro Bloco IF #############################################   
else :
        print("você perdeu o premio:")
