# Funçao é uma coleção de código que executa uma tarefa específica
#Básico sobre funçao no python

#def e usado para declarar funcao, exemplo de sintaxe abaixo

# def function_name():
# def = sintaxe para começar declarar que é uma funçao
# funcion_name = nome da minha funçao
# : = declara que oq vier abaixo é código dessa funçao criada


def diga_oi():
  print("olá usúario")
  
diga_oi() #executa a chamada da funçao para ela funcionar


print("top") #teste para ver ordem de leitura de execução
diga_oi() #executa a chamada da funçao para ela funcionar
print("bottom") #teste para ver ordem de leitura de execução

#função com paramentros
def diga_oi_2(name): 
  print("olá, " + name + "\n\n")


diga_oi_2("Pedro") #como foi definido um parametro, dentro da chamada passo o valor do paramentro
#resultado da execução da funcao diga_oi_2 = olá, Pedro
diga_oi_2("Mike") #como foi definido um parametro, dentro da chamada passo o valor do paramentro
#resultado da execução da funcao diga_oi_2 = olá, Mike

#teste com mais paramentros
def diga_info(name, age, weight):
  #lógica simples para testar comportamento da funçao em python com vários parametros
  print("Olá," + name + "\nVí aqui que você tem: " + age + " Anos de idade" + "\nTambém notei que seu peso é: " + weight + "Kg")
  input(name + ", Você confirma esses dados? sim ou nao :\n")
  print("Obrigado pela resposta, " + name + "!  :)")
    
diga_info("Pedro", "24", "68") # chamando a função e passando os valores dos paramentros

#Caso passar em numero, e necessário converter para string por exemplo, para ficar padronizado e poder fazer concatenaçao

