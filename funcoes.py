from Utilidades import apresentação

acertos = list()
erros = list()

def leia_letra(mensagem):
    while True:
        letra = str(input(mensagem))
        if len(letra) == 0:
            print("\033[31mSeu palpite não pode ser vazio. Tente novamente.\033[m")
            continue
        if len(letra) > 1:
            print("\033[31mDigite apenas uma letra. Tente novamente.\033[m")
            continue
        if letra.isnumeric():
            print("\033[31mNúmeros não são permitidos. Tente novamente.\033[m")
            continue
        if letra.isalpha():
            return letra

def sorteio():
    from random import choice
    tupla = ("palavra", "algodao", "abacaxi", "liquidificador", "paralelepipedo", "asfalto", "carro", "bicicleta")
    palavra = choice(tupla)
    return palavra
    
def show(palavra, letra):
    """Essa função mostra a palavra na tela e verifica a vitória. Essa função foi corrigida pelo Gemini
    Parâmetro palavra: recebe a palavra a ser advinhada.
    Parâmetro letra: recebe o palpite do jogador.
    Return: retorna False sempre."""
    palavra_lista = list(palavra)
    if letra in palavra:
        acertos.append(letra)
    if letra not in palavra_lista:
        erros.append(letra)
    vitória = True
    for i in palavra_lista:
        if i in acertos:
            print("\033[34m", end="")
            print(f"{i} ", end='')
            print("\033[m", end="")
        else:
            print("\033[31m", end='')
            print("_ ", end='')
            print("\033[m", end="")
            vitória = False
    print()
    
    
    if vitória:
        apresentação.adaptado("RESULTADO")
        print("\033[35mParabéns! Você ganhou\033[m")
        return False
    if len(erros) == 6:
        apresentação.adaptado("RESULTADO")
        print("\033[35mVocê perdeu\033[m")
        return False
        