#COMO OBTER ENTRADA DE UM USUÁRIO

#PERMITIREMOS QUE O USUARIO INSIRA INFORMAÇÕES NO NOSSO PROGRAMA E PEGAR ESSAS INFORMAÇÕES E ARMAZENA-LAS EM VARIÁVEIS
#SENDO ASSIM PODEMOS PEGAR AS INFORMAÇOES E FAZER ALGO COM ELAS

# input() #diz ao python que queremos obter entradas de um usuário, e ele permite que o usuário digite algumas informações



#Criando um pequeno aplicativo python que permitirá o usuário inserir seu nome, armazenaremos o dado em uma variavel e vou dar oi para ele

name = input("Digite seu nome: ") #pego o nome que ele vai inserir e armazeno na variavel name
print("Olá " + name + ", é um prazer te-lo aqui !") # imprime a frase olá {name}, é um prazer te-lo aqui

#teste um pouco com mais variáveis

name2 = input("Digite seu nome aqui: ")
age = input("agora digite sua idade: ")
peso = input("Qual seu peso em kg? ")

print("Olá " + name2 + ", vi aqui seus dados e percebi que:\n""Sua idade atual é: " + age +"\nE seu peso atual é: " + peso)
confirmation = input("Voce confirma esses dados?")
print("Resposta: " + confirmation+ "\nObrigado pela Resposta")

# fazendo uma calculadora classica com inputs , variaveis e matematica

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero numero: ")
result1 = int(num1) + int(num2)
result2 = int(num1) * int(num2)

print ("A soma desses números é: " + str(result1) )
print ("\n A multiplicação desses numeros é:\n" + str(result2) )