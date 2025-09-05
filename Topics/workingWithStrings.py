# \n Adiciona quebra de linha
print("E ai Pedro\nTudo bem?")

#colocar aspas "" dentro de uma string.
#utilizando caractere de scape, \ (BARRA INVERTIVA) + CARACTERE.
#isso diz ao python que apos a barra, qualquer caractere q venha significa que quero renderiza-lo
print("Pedro\"Ferreira\"")

print("Pedro\Ferreira") #assim imprime apenas a barra invertida.

frase = "Está estudando python"

print(frase) #resultado é o print do valor da variável
print("Pedro " + frase) #resultado é a concatenaçao da string "pedro" + o valor da variável.
print(frase + ", o Pedro") #resultado é a contatenação do valor da variável primeiro + o valor da string ", o Pedro".

#funcoes comuns que podemos usar com a string

print(frase.lower()) # .lower vai fazer com que a string armazenada na variavel frase seja toda em letra minúsculas
print(frase.upper()) # .upper vai fazer com que a string armazenada na variavel frase seja toda em letra MAIUSCULA
print(frase.isupper()) # .isupper me retorna um booleano verdadeiro ou falso, perguntando se a frase é toda em letra maiuscula
#no caso acima é false o resultado pois apenas a primeira letra na variavel esta em maiuscula.

print(frase.upper().isupper()) # utilizando essas funçoes em conjunto, primeiro peguei o frase e transformei toda em letra maiúscula, e após isso
#pedi para verificar se TRUE OU FALSE, a string esta em letra maiuscula, resultado TRUE.
print(len(frase)) #função de comprimento, me diz quantos caracteres há dentro dessa string

print(frase[0]) #Capturo o caractere especifico que quero, 0 = primeiro caractere, 1 = segundo caractere ... resultado "E"
print(frase[3]) #Capturo o caractere especifico que quero, querto caractere. resultado "á"

# FUNÇÃO INDEX

print(frase.index("p")) #dentro do paramentro "()" especifico oque eu quero obter e ele me diz em qual posição esta no lenght(len) resultado 15
print(frase.index("Está")) #dentro do paramentro "()" especifico coloquei uma palabra completa e ele me diz em qual posição esta no lenght(len). ONDE COMEÇA. resultado 0
print(frase.replace("Está", "Estou")) #usando funçao replace para substituir algo, no caso peguei a palavra "Está" dentro da minha variável
# e substitui ela pela palavra "Estou". resultado é a frase modificada apenas onde especifiquei e o resto continua como antes



# TODAS FUNCÇOES internas de Manipulação de Strings (built-in) 
#Funções que ja vêm com o python, sempre disponíveis para uso

# 1. Funções de Manipulação de Strings
frase2 = "  olá, Python!"
print(f"Original: '{frase2}'")

# .upper(): Retorna a string em maiúsculas.
print(f"str.upper(): {frase2.upper()}")
# Resultado:   OLÁ, PYTHON!

# .lower(): Retorna a string em minúsculas.
print(f"str.lower(): {frase2.lower()}")
# Resultado:   olá, python!

# .strip(): Remove espaços em branco do início e do fim.
print(f"str.strip(): {frase2.strip()}")
# Resultado: olá, Python!

# .replace(antigo, novo): Substitui partes da string.
print(f"str.replace(): {frase2.replace('Python', 'Mundo')}")
# Resultado:   olá, Mundo!

# .split(separador): Divide a string em uma lista de strings.
texto_longo = "Python é uma linguagem de programação"
lista_palavras = texto_longo.split(" ")
print(f"str.split(): {lista_palavras}")
# Resultado: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']