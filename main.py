import funcoes
from Utilidades import apresentação

palavra = funcoes.sorteio()

apresentação.cabeçalho("JOGO DA FORCA")
while True:
    letra = funcoes.leia_letra("\033[36mQual é o seu palpite? \033[m")
    final = funcoes.show(palavra, letra)
    if not final:
        break
        
apresentação.cabeçalho("OBRIGADO POR JOGAR")
    
    