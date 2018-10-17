" Programa calcula os ganhos e perdas do mês das empresas"
i = 1
ganho = 0
gasto = 0
balanca = 0

print("\t\t Calculo de lucratividade das empresas ao mês\n\n")
empresa = int(input("Digite o numero da empresas: "))
meses = int (input("Digite a quantidade de meses: "))

while i < empresa:
    print("empresa {}\n".format(i))
    j = 0
    
    while j < meses:
        print("Mês {}".format(j))
        ganho= int(input("Digite o ganho da empresa no mês: "))
        gasto= int(input("Digite o gasto da empresa no mês: "))
        balanca = balanca +(ganho-gasto)
        j= j+ 1

        
        if balanca > 0 :
            print(" A empresa lucrou {}".format(balanca))
            print("\n")
        elif balanca == 0:
            print(" A empresa ficou indiferente, com o valor {}".format(balanca))
            print("\n")
        else: 
                print(" A empresa ficou com um deficit de {}".format(balanca))
                print("\n")
    i=i+1
       

