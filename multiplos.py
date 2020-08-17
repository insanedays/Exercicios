
print("DESAFIOS DE NÍVEL 1 - PHYTON 3")


def divisores():
    print("Desafio 1: divisores de 7 que nao são por 5")

    numeros_desafio = []
    for n in range(200, 3201):
        if (n%7==0) and (n%5!=0):
            numeros_desafio.append(n)

    print("RESPOSTA DESAFIO 1:", numeros_desafio)





#Desafio 2: fatore qualquer número#
print("Desafio 2: Fatoração")
def fat():
    n = input("Digite um número:")
    n = int(n)

    if ( n == 0):
      print("Fatoração = 0")
    elif(n==1):
      print("Fatoração = 1")
    else :
        theFactors = []
        for i in range(2,n+1):
            while n % i == 0:
                n = n/i
                print(i)
                theFactors.append(i)
    i = int(i)
    sobrou = print("Sobrou", n)
    print("RESPOSTA DESAFIO 2:", theFactors)


#Desafio 3

def append_list():
    numero_digitado = int(input("Digite aqui um número:"))

    x = []

    for numero_ql in range(1, numero_digitado + 1):
        x.append(numero_ql)
        y = numero_ql * numero_ql
        x.append(y)
    print(x)

    #Questão 4


print("Questão 4:")

def substituicao_lista():
    j = [14, 15, 17]

    t = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t[3:10] = []
    print(t)

    j = str(j)

    y = j.strip("a")

    print(y)

def calculo_salario ():
    salario_hora = int(input("Quanto você ganha por hora?"))
    horas_trabalhadas = int(input("Quantas horas trabalha no mês?"))

    salario_bruto = salario_hora * horas_trabalhadas
    percent_ir = 0.11 * salario_bruto
    percent_inss =  0.08 * salario_bruto
    percent_sindicato = 0.05 * salario_bruto

    salario_liquido = int(salario_bruto - percent_ir - percent_inss - percent_sindicato)

    print("Seu salário descontando os impostos é de:", salario_liquido)



