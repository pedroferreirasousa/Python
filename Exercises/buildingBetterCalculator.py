# Calculadora capaz de realizar todas as operações aritméticos basicas:
# SOMAR, SUBTRAIR, MULTIPLICAR, DIVIDIR
# Permitiremos que o usuario escolha qual tipo de opração ele quer realizar e define seus numeros

num1 = float(input("Digite o primeiro numero: ")) # utilizo o float para que tudo que o usuario escrever sera convertido em um Numero!
operador = input("Digite um operador: ") # Obtenho o operador aritmético
num2 = float(input("Digite o segundo numero: ")) # utilizo o float para que tudo que o usuario escrever sera convertido em um Numero!

if operador == "+":
  print(num1 + num2)
elif operador == "-":
  print(num1 - num2)
elif operador == "*":
  print(num1 * num2)
elif operador == "/":
  print(num1 / num2)
else:
  print("Operador inválido, utilize sinais matemáticos ( +, -, * ou / ) para que seja possível calcularmos")
  
  