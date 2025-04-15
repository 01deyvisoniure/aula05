alunos=int(input("digite a quantidade de alunos: "))
i=0
soma=0
while i <alunos:
    nota=float(input("digite  a nota do aluno: "))
    soma+=nota
    i+=1
media=soma/alunos
print("media da sala: ",media)