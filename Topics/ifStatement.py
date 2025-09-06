# No Python, a instrução if é usada para tomar decisões no código.
# Ela permite que um programa escolha diferentes caminhos de execução com base em uma condição lógica 
# (algo que pode ser True ou False).
# Em outras palavras: o if pergunta “essa condição é verdadeira?”
# Se sim, o bloco de código dentro dele é executado.
# Se não, ele é ignorado e o programa continua normalmente.

#instruções:
# if → executa um bloco de código se a condição for verdadeira.
# else → executa se nenhuma condição anterior foi satisfeita.
# elif → permite testar várias condições em sequência.

#SINTAXE BASICA

#if condição:
    # código a ser executado se a condição for verdadeira
    

#Exemplo simples com If

idade = 18

if idade >= 18: #SE ESSE CASO FOR VERDADE, A MENSAGEM ABAIXO É EXIBIDA
    print("Você é maior de idade") #MENSAGEM EXIBIDA POIS A IDADE É 18, PARA SER EXIBIDA TERIA Q SER 18 OU MAIOR QUE 18
    

#Exemplo simples com else

idade2 = 16

if idade2 >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    #Resultado "Menor de idade", pois como nao se encaixou no "SE FOR MAIOR OU IGUAL A 18", como nao se encaixou nessa condição temos o 
    #else para retornar "menor de idade"
    
    
#Exemplo simples com elif (else if)

nota = 7

if nota >= 9:
    print("Ótimo!")
elif nota >= 7:
    print("Bom!")
else:
    print("Precisa melhorar")
    #resultado "BOM", pois esta dentro da condição de maior ou igual a 7, porem fora da condição de maior ou igual a nove ou menor que 7 (caso else)
    #pois variavel nota é de valor =7
    
    
# O if é como um semáforo no trânsito:

# Se o sinal está verde → você segue.
# Se está vermelho → você para.
# Se está amarelo → você decide com base em outra regra.

# mais exemplos

is_male = True
is_tall = False

if is_male and is_tall:
  print("voce é homem alto")
elif is_mate and not(is_tall):
  print("Voce e homem, mas nao e alto")
elif not(is_male) and is_tall:
  print("Voce nao e homem, mas é alto")
else:
  print("você nao e homem e nem alto")
  
  #tradução facil entendimento:
  
# se é homem e é alto:
#   mostre("Voce e um homem alto")
# caso seja homem e nao seja alto:
#   mostre("voce e homem, mas nao e alto")
# caso nao seja homem mas seja alto:
#   mostre("voce nao e homem mas e alto")
# se nao:
#   mostre("voce nao e homem e nem alto")
