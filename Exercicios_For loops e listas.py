
Notas= []
soma_nota = 0
QtdeMaior7=0
print("\t\t Calcula a Nota dos Alunos\n\n")

for i in range(1,10+1):
    print("Aluno ",i)
    media = 0
    soma_nota = 0
    for j in range(4):
        nota=int(input("Digite a nota: "))
        soma_nota = nota  +   soma_nota
    media= soma_nota/4
    Notas.append(media)
    print(" ")
for i in range(len(Notas)):
    if Notas[i] > 7 :
        QtdeMaior7 += 1
print("A quantidade de alunos com media maior que 7 é: ",QtdeMaior7)
print(Notas)
