

#fazendo comparaçao dentro de if, elif e elso


#teste para função retornar o maior numero

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3: #se num 1 for maior ou igual a num2 e num1 for >= num3. return num1 ( porque ele e o maior)
    return num1
  elif num2 >= num1 and num2 >= num3: #se num2 for maior ou igual a num1 e num2 for maior ou igual num3. return num2 ( porque ele e o maior)
    return num2
  else: # se passou por essas condiçoes e nao retornou nada, e porque o num3 é o maior, entao retorne ele
    return num3;
  
print(max_num(124, 546, 2355)) # Nesse caso o resultado é o num3 ( 2355 ) como maior numero
print(max_num(3455, 2331, 32)) # nesse caso o resultado é o num1 (3455) como maior numero
print(max_num(42, 32212, 332)) # Nesse caso o resultado é o num2 (32212) como maior numero
print(max_num(223, 223, 4)) # nesse caso o meior numero é (223)

#Pode-se comparar outros tipos, por exemplo, string, boolean etc..

# Atribuição (NÃO é comparador!!!!!!)
x = 10                  # =    atribui o valor 10 à variável x (não compara)

# Igualdade / Desigualdade
x == 10                 # ==   True se os valores forem iguais (usa __eq__ do tipo) 
# "5" == 5 resultado é : False (str vs int, tipos diferentes → não converte)

x != 5                  # !=   True se os valores forem diferentes

# Comparações relacionais
x > 5                   # >    True se x for maior que 5
x < 20                  # <    True se x for menor que 20
x >= 10                 # >=   True se x for maior ou igual a 10
x <= 9                  # <=   True se x for menor ou igual a 9

# Identidade de objeto (mesmo objeto na memória)
a is b                  # is   True se a e b referenciam o mesmo objeto (mesmo id)
a is not b              # is not True se a e b NÃO são o mesmo objeto

# Membros / Associação
item in colecao         # in   True se item está presente em colecao (lista, set, str, dict keys, ...)
item not in colecao     # not in True se item NÃO está presente em colecao

# Exemplo de encadeamento (útil e elegante)
1 < x <= 100            # equivalente a (1 < x) and (x <= 100), avaliado de forma encadeada

# Comparações entre sequências (strings, listas) são lexicográficas
"abc" < "bcd"           # compara pelos códigos de caracteres (ordem lexicográfica)
[1, 2] < [1, 3]         # compara item a item

# Observações importantes
# - Para checar None use 'is None' (recomendado):  if valor is None: ...
# - '==' verifica igualdade de valor (usa método __eq__); 'is' verifica identidade (mesmo objeto).
# - Evite comparar floats com '==' por imprecisão; prefira math.isclose(a, b).
# - Comparar tipos incompatíveis (ex: 3 < "a") lança TypeError em Python 3.
# - O operador '<>' não existe em Python 3 (era válido em Python 2).

