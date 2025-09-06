# Uso de intrução Return dentro de um codigo python

# Basicamente a funçao python é apenas a coleção de codigo python que executa uma tarefa espeficia
# Quando queremos executamos essa tarefa no nosso python/programa podemos chamar uma função python
# Muitas vezes apenas chamamos a funçao e ela faz oque quer
# Mas as vezes quando chamamos uma função queremos obter informações dessa função,
# Entao quando, executamos uma função quero que basicamente execute sua tarefa/ todo codigo da função e entao quero que me de alguma
# informação de volta, resumidamente (apos a execução) no return é como se ele dissese "ei aqui esta algumas informações"
# utilizando a palavra chave de instrução return
# Destacar o efeito do return: ele não só "entrega" informação, mas também encerra a execução da função.


#ex:

def somar(a,b):
  return a+b #digo "Retorne a + b,"

resultado = somar(2,3) #variável resultado é igual a funçao de somar criada a cima, com os paramentos de 2 e 3 para serem somados
print(resultado)  # resultado da resposta de variavel resultado "5"

resultado2 = somar(10, 11) # segunda variavel usando a mesmça função
print(resultado2) # resultado da resposta da segunda variavel "21" somou os paramentros 10 e 11


#exemplo função de elevar um numero ao cubo

def cube(num):
  return num*num*num

print(cube(3))

#LEMBRANDO QUE APÓS O RETURN É ENCERRADO A FUNÇÃO