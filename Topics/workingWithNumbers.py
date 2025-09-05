#IMPORT NO PYTHON
from math import * #importando metodos math necessario para acessar mais metodos
#quando colocamos a linha de codigo de import no codigo e nos da acesso a muita mais chamadas

print(2) # apenas imprimindo numero inteiro
print(2.0987) # imprimindo numero decimal
print(-2.98) #imprimindo numero negativo

print (3 + 4.5) #imprimindo resposta de soma

#operadores matematicos simples + - / *

#reconta mais complexas sao aceitas, especificando ordem etc...
print(10 + (3 * 5) - 4)

my_num = 5
print(my_num)

# converter numero para string

print (str(my_num)) # converti o valor da variavel my_num que era um numero em uma string
# print(my_num + "numero")  <-  esse explempo da erro pois estou tentando somar um numero com uma string.
print(str(my_num) + " Meu Número agora e uma string") #nesse caso da certo pois transformei meu numero em uma string antes de somar com outra string

#Métodos mais comuns utilizada em python

my_num2 = -5 #valor negativo

print(abs(my_num2)) # funçao abs me da o valor absoluto, mesmo o numero sendo negativo na variavel o resultado é 5 pois e seu valor absoluto

print(pow(3, 2)) #funçao pow me permite elevar um numero, primeiro paremetro e o numero e o segundo e o elevado, no caso peguei o numero 3 e elevei a 2, resultado 9

print(max( 1,4, 6)) #funçao max me retorna o maior numero do paramentro, primeiro paremetro , resultado 6. posso passar quantos paramentros eu quiser

print (min(1, 4, 6)) #função min me retorna o menor numero do parametro, no caso o oposto da funçao max, resultado 1

print (round(3.2)) # função round arredonda o numero decimal, resultado 3
print (round(3.6)) # função round arredonda o numero decimal, como passou do 5 o arredondado é 4


#AQUI JA ESTAMOS UTILIZANDO OS METODOS IMORTADOS LA EM CIMA

print(floor(3.7)) # metodo que pega o menor numero, cortando o .  resultado 3
print(ceil(3.7)) # metodo que faz o oposto do floor, resultado 4, pois foi arrendondado

print(sqrt(36)) # metodo retorna a raiz quadrada do numero, resultado 6. pois q raiz quadrada de 36 é 6


#MAIS FUNCOES PEGANDO PELO IMPORT
# Outra forma de importar é pegar funções específicas, assim:

# Primeiro, vamos garantir que temos acesso à biblioteca math.
import math
# from math import floor, ceil, pi, e

# --- Funções Trigonométricas ---

# Retorna o cosseno de x (em radianos).
print(f"Cosseno de 0: {math.cos(0)}")

# Retorna o seno de x (em radianos).
print(f"Seno de pi/2: {math.sin(math.pi / 2)}")

# Retorna a tangente de x (em radianos).
print(f"Tangente de pi/4: {math.tan(math.pi / 4)}")

# Retorna o arco cosseno de x, em radianos.
print(f"Arco cosseno de 1: {math.acos(1)}")

# Retorna o arco seno de x, em radianos.
print(f"Arco seno de 1: {math.asin(1)}")

# Retorna o arco tangente de x, em radianos.
print(f"Arco tangente de 1: {math.atan(1)}")

# Converte um ângulo de graus para radianos.
print(f"90 graus em radianos: {math.radians(90)}")

# Converte um ângulo de radianos para graus.
print(f"Pi radianos em graus: {math.degrees(math.pi)}")

# --- Funções Exponenciais e Logarítmicas ---

# Retorna e**x (a função exponencial).
print(f"e elevado a 1: {math.exp(1)}")

# Retorna o logaritmo natural de x (base e).
print(f"Logaritmo natural de e: {math.log(math.e)}")

# Retorna o logaritmo de x para uma dada base.
print(f"Logaritmo de 100 na base 10: {math.log(100, 10)}")

# --- Outras Funções Úteis ---

# Retorna o valor absoluto de x. Você já usou a função embutida `abs()`, mas `math.fabs()` é outra opção.
print(f"Valor absoluto de -10.5: {math.fabs(-10.5)}")

# Retorna o fatorial de x.
print(f"Fatorial de 5: {math.factorial(5)}")

# Retorna o máximo divisor comum dos inteiros a e b.
print(f"MDC de 48 e 18: {math.gcd(48, 18)}")

# Retorna o valor de x elevado à potência de y. Similar a `pow()`, mas `math.pow()` funciona apenas com floats.
print(f"2 elevado a 3: {math.pow(2, 3)}")

# --- Constantes Matemáticas Importantes ---

# A constante matemática pi (π).
print(f"O valor de pi é: {math.pi}")

# A constante matemática e.
print(f"O valor de e é: {math.e}")

# A constante para o infinito.
print(f"1 bilhão é maior que o infinito? {1000000000 > math.inf}")
