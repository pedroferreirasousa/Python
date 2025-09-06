#Lista é uma estrutura para armazenar lista de informações, permitindo organizar e acompanhar os dados mt mais facil

amigos = ["Neto", "Milena", "Thiago", "Junior"]
#           0        1         2         3

print(amigos)
print(amigos[0])
print(amigos[-1]) # valor negativo pega do final # resultado "Junior"
print(amigos[1:]) # pega o index 1 e os proximos # resultado Milena,Thiago,Junior
print(amigos[0:3]) # pega todos elementos pelo index desde o 0 até o 2, para no 3

amigos[1] = "teste" #altera o valor de um elemento específico dentro da lista, #resultado alterei o index 1(Milena) para Teste
print(amigos[1])

#lista aceita varios tipos
lista_teste = [ "string", 3, False]

print(lista_teste)



#FUNÇÕES DE LISTA

numeros = [4, 8, 15, 16, 23, 42]
nomes = ["Pedro", "João", "José", "Maria", "Oscar", "Pedro"]
variavel_test = [1, 4, "Teste", True]
variavel_test2 = [1, 2, 3, 4, 5]
nomes2 = ["Pedro", "João", "José", "Maria", "Oscar", "Pedro"]
nomes_copy = [ ]

#.extend()
nomes.extend(numeros) # extends faz extenção da lista, ao usa-lo junta-se o conteúdo de uma lista com a outra # resultado = "Pedro", "João", "José", "Maria", "Oscar", 4, 8, 15, 16, 23, 42 
print(nomes)

#.append()
numeros.append(98) # permite adicionar mais item no final da lista com um valor específico # RESULTADO = 4, 8, 15, 16, 23, 42, 98
print(numeros)

#.insert()
variavel_test.insert(1, "adicionado no index 1") # permite adicionar item na lista na posição que deseja, primeiro paramentro define a posição
# que vai ser inserido, o segundo paramentro define o valor que vai ser inserido, resultado =  "adicionando no index 1" ficou no index 1
# e todos intens posterios sao "empurrados", passa a ter um novo index maior.
print(variavel_test)

#.remove
variavel_test.remove("adicionado no index 1") # remove elementos da lista
print(variavel_test) #resultado removido o elemento 

#posso limpar a lista inteira tambem deixando o paramentro vazio com a function "clear"

#.clear()
variavel_test.clear()
print(variavel_test) #resultado = lista vazia foi limpada

#.pop() 
variavel_test2.pop() # remove o ultimo elementro da lista, no caso da variavel_test2 = [1, 2, 3, 4, 5], resultado é variavel_test2 = [1, 2, 3, 4]
print(variavel_test2)

#.index()
print(nomes.index("Pedro")) # retorna o index do valor especifico dentro da lista que foi passado no paramentro, e muito
#utilizado para verificar se o item ja exista em uma lista mt grande, se retornar algum valor é pq exista Resultado = 0 (index 0 para valor Pedro)
#caso 2 se colocar um um valor que nao exista retorna que o valor nao ta na lista

#.count()
print(nomes.count("Pedro")) # Conta quandos itens iguais tem na lista, como na variavel tem 2 Pedros o retorno é 2

#.sort()
nomes2.sort() # Classifica a lista e organiza, no caso especifico a lista de string e retornada em ordem alfabetica
print(nomes2) #retornou ['José', 'João', 'Maria', 'Oscar', 'Pedro', 'Pedro'] em ordem alfabetica, obs. nao da para utilizar com tipos diferentes na lista ex : lista com string e numeros

#.reverso()
nomes2.reverse() # reverte a ordem da lista, ultimo passa ser primeiro, penultimo em segundo etc...
print(nomes2)

#.copy() 
nomes_cop = nomes2.copy() # defini para a variavel nomes_copy o valor copiado da variavel nomes2 atual
print(nomes_copy)



# COMPLEMENTOS PEGO COM IA

# --- Outros Métodos e Técnicas de Manipulação de Listas ---

# Listas aninhadas: uma lista pode conter outras listas.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Lista aninhada: {matriz}")
print(f"Acessando o primeiro elemento da primeira sub-lista: {matriz[0][0]}")
# resultado: 1

# List comprehension: uma forma concisa de criar listas.
# Exemplo: criar uma lista com o quadrado dos números de 0 a 4.
quadrados = [x**2 for x in range(5)]
print(f"Lista criada com list comprehension: {quadrados}")
# resultado: [0, 1, 4, 9, 16]

# --- Funções Embutidas que Funcionam com Listas ---

# len()
# Retorna o número de elementos na lista.
print(f"A lista 'nomes2' tem {len(nomes2)} elementos.")
# resultado: 6

# sum()
# Retorna a soma de todos os itens de uma lista de números.
numeros_novos = [10, 20, 30]
print(f"A soma dos números é: {sum(numeros_novos)}")
# resultado: 60

# min() e max()
# Você já viu essas funções, mas elas funcionam perfeitamente com listas.
print(f"O menor número na lista 'numeros_novos' é: {min(numeros_novos)}")
# resultado: 10
print(f"O maior número na lista 'numeros_novos' é: {max(numeros_novos)}")
# resultado: 30

# sorted()
# Retorna uma nova lista com os itens da lista original em ordem crescente,
# sem modificar a lista original.
lista_desorganizada = [5, 1, 9, 3, 7]
lista_organizada = sorted(lista_desorganizada)
print(f"Lista original: {lista_desorganizada}")
# resultado: [5, 1, 9, 3, 7]
print(f"Nova lista organizada: {lista_organizada}")
# resultado: [1, 3, 5, 7, 9]

# --- Métodos de Lista Avançados ---

# .reverse() (semelhante a reverse, mas como método)
# Reverte a ordem dos elementos da lista no lugar, ou seja,
# modifica a lista original.
numeros_reverso = [1, 2, 3, 4]
numeros_reverso.reverse()
print(f"Lista revertida no lugar: {numeros_reverso}")
# resultado: [4, 3, 2, 1]

# .clear()
# Você já usou esta, mas é importante reforçar que ela remove
# todos os itens da lista, deixando-a vazia.
# (Já coberto no seu código, mas mantido para referência)

# .count()
# Você também já usou esta, mas é uma função poderosa.
# (Já coberto no seu código, mas mantido para referência)

# .index()
# Você já usou esta, mas é bom lembrar que ela encontra
# a primeira ocorrência do valor. Se houver valores duplicados,
# ela retorna apenas o índice do primeiro.
# (Já coberto no seu código, mas mantido para referência)

