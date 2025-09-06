#DICIONARIOS EM PYTHON
#ESTRUTURA ESPECIAL EM PYTHON QUE NOS PERMITE ARMAZENAR INFORMAÇÕES NAS CHAMADAS "VALOR DE CHAVES PARES"

#BASICAMENTE POSSO APENAS CRIAR UM MONTE DESSES DIFERENTES PARES DE VALORES CHAME E QUANDO QUISER ACESSAR UMA INFORMAÇAO ESPECIFICA
#DENTRO DO DICIONARIO POSSO APENAS SE REFERIR A ELE POR SUA CHAVE


#SIMILAR AO DICIONARIO NORMAL:
#TENHO UMA PALAVRA E TENHO UMA DEFINIÇAO ASSOCIADA A ESSA PALAVRA EX. (PARAVRA = DENIFICAO DE PALAVRA)
#NESSA SITUAÇÃO A PALAVRA E OQ CHAMAMOS DE "CHAVE" E O "VALOR" DA CHAVE SERIA A DEFINIÇÃO

#EXEMPLO: 
#CRIAÇÃO DE PROGRAMA QUE PERMITE CONVERTER UM NOME DE MES DE 3 DIGITOS APENAS NO NOME DE MES COMPLETO
# tipo = jan -> janeiro; fev -> fevereiro ; etc...

# monthConversions = {} #modelo de criaçar de dicionario

monthConversion = {
  "Jan": "Janeiro",
  "Fev": "Fevereiro",
  "Mar": "Março",
  "Abr": "Abril",
  "Mai": "Maio",
  "Jun": "Junho",
  "Jul": "Julho",
  "Ago": "Agosto",
  "SET": "Setembro",
  "Out": "Outubro",
  "Nov": "Novembro",
  "Dez": "Dezembro",
}

print(monthConversion) # Resultado todos valores armazenados no dicionario
print(monthConversion["Nov"]) # Resultado = valor associado a "Nov" ... "Novembro"
print(monthConversion["Mar"]) # Resultado = valor associado a "Mar"... "Março"

#Usando .get
print(monthConversion.get("Mar")) # resultado = Março

# Usando o get pode-se especificar um valor padrão que eu quero.
print(monthConversion.get("Pedro")) # Coloquei como valor Pedro, que nao existe e nao da pra ser mapeado dentro do Dicionario
#Posso adicionar um valor padrao de resposta no sengundo paramentro EX:
print(monthConversion.get("Pedro", "Pedro não é uma chave valida ")) # resultado = "Pedro nao é uma chave valida"

#POSSO USAR NUMEROS TB... EX:

monthConversionNum = {
  0: "Janeiro",
  1: "Fevereiro",
  2: "Março",
  3: "Abril",
  4: "Maio",
  5: "Junho",
  6: "Julho",
  7: "Agosto",
  8: "Setembro",
  9: "Outubro",
  10: "Novembro",
  11: "Dezembro",
}

print(monthConversionNum.get(1)) #Resultado Fevereiro
#ou
print(monthConversionNum[0]) #Resultado Janeiro
#