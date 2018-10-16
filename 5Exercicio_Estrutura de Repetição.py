
print("\t\tDiz se o numero é centena ,dezena  ou milhar\n")

valor = int(input("Digite um numero abaxio de 1000: "))


if valor ==1000 :
    print("milhar");
if valor >=  100 :
     resto = valor%100
     ValorSeco= valor - resto
     centena =   ValorSeco/100
     print( "A centena é: {}".format(centena) )

   
     restodezena = resto%10
     valorSeco = resto -   restodezena
     dezena = ValorSeco/100
     print("A dezena é : {}".format(dezena))
     print("A unidade é: {}".format(restodezena))
        

    
   
