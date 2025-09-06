# Ideia do jogo, Usúario deve adivinhar a palavra secreta


# Criar um "mini game", onde defino uma palavra secreta, e o usuario tem que acertar essa palavra que guardei na variavel palavra_secreta
#enquando o palpite for diferente da palavra secreta ele continua recebendo a mensagem para digitar um palpite
#quando for igual, ele recebe a resposta de que acertou a palavra

#variaveis
palavra_secreta = "joelho" # definido a palavra secreta que o usuario terá que acertar
palpite = "" #váriavel para armazenar resposta do usuario

while palpite != palavra_secreta:
  palpite = input("Digite o palpite: ")
  
print("Parabens! Você acertou a palavra secreta: " + palavra_secreta)


#MELHORIAS NO JOGO ADICIONANDO LIMITE DE 3 TENTATIVAS
#Adicionando logica de if else se caso palmites acabou ou se caso acertou a resposta
# necessario definir mais variaveis para a estruturação da logica do jogo

palavra_secreta = "pedro"
palpite = ""
contagem_palpites = 0
limit_of_palpites = 3
acabou_palpites = False

while palpite != palavra_secreta and not(acabou_palpites):
  if contagem_palpites < limit_of_palpites:
    palpite = input("Digite um palpite do nome do desenvolvedor:")
    contagem_palpites += 1
  else:
    acabou_palpites = True
    
if acabou_palpites:
  print("Acabou o limite de 3 palpites e voce perdeu")
else:
  print("Você venceu, acertou o nome do desenvolvedor " + palavra_secreta)
