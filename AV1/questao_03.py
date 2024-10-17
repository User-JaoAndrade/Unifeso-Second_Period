# Implemente um jogo da forca para dois ou mais jogadores com uma temática
# personalizada. O programa deve permitir que um dos jogadores insira uma palavra e
# dicas e o(s) outro(s) jogador(es) tente(m) adivinhá-la dentro de um limite máximo de
# tentativas pré-estabelecido (i.e. a formação do boneco na forca). Adicione um sistema
# de pontuação que se baseie no número de tentativas e na dificuldade da palavra. No
# final de cada rodada (i.e. o boneco foi formado por completo ou alguém descobriu a
# palavra), o sistema deverá exibir o ranking dos jogadores, ordenados em ordem
# decrescente com base na quantidade de pontos.

import os
import time
import typing

# Função para limpar o terminal
def limpando_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para limpar n linhas do terminal
def limpar_linhas(n: int) -> None:
    for _ in range(n):
        print("\033[F\033[K", end='')

# Início do programa / definindo jogadores
def main() -> None:
    limpando_terminal()
    num: int = 0

    print(" >>> JOGO DA FORCA <<< ")
    try:
        numero_de_jogadores: int = int(input("Informe o número de jogadores (informe ao menos 2 jogadores): "))

        if numero_de_jogadores < 2:
            print("Por favor, informe mais de um jogador")
            for letra in "Retornando": 
                print(letra, end='')
                time.sleep(0.4)
            main()
        else:
            # Cadastrando jogadores
            while num < numero_de_jogadores:
                limpando_terminal()
                print(">>> CRIANDO PERFIS DE JOGADORES <<<")

                num += 1

                # Pedindo nome para o jogador
                nome: str = input(f"\nInforme o nome do jogador {num}: ")
                while nome in jogadores.keys():
                    nome = input("\nJogador já cadastrado, informe outro nome: ")
                
                # Adicionando o novo jogador ao dicionário
                jogadores[nome] = 2000

            segredo_de_estado()

    except ValueError:
        print("INFORME UM VALOR VÁLIDO")
        for letra in "Retornando": 
            print(letra, end='')
            time.sleep(0.4)
        main()

# Função para definir a palavra secreta
def segredo_de_estado() -> None:
    limpando_terminal()
    vilao: str = next(iter(jogadores))

    print(f"Jogadores: {list(jogadores.keys())}")
    print(f"\n>>> '{vilao}' é o vilão e está tentando enforcar uma pessoa <<<")
    
    palavra_secreta: str = input("\nPALAVRA SECRETA: ")
    limpar_linhas(1)

    # Verificando se tem espaço na palavra secreta
    while ' ' in palavra_secreta:
        palavra_secreta = input("Não coloque espaços, apenas uma palavra: ")
        limpar_linhas(1)
    dica: str = input("Dica da palavra secreta: ")

    if len(palavra_secreta) <= 6:
        diminuindo_pontos: int = 5
    elif len(palavra_secreta) > 6 and len(palavra_secreta) <= 8:
        diminuindo_pontos: int = 7
    else: 
        diminuindo_pontos: int = 10

    game(palavra_secreta, diminuindo_pontos, dica)

# Função de jogo
def game(palavra_secreta: str, diminuindo_pontos: int, dica: str) -> None:
    # Jogo
    for jogador, pontos in jogadores.items():
        limpando_terminal()

        # Pula o vilão
        if jogador == next(iter(jogadores)):
            continue

        tentativas: int = 6
        letras_jogadas: typing.List[str] = []  # Registro de letras jogadas
        acertou_palavra: bool = False

        # Jogador x jogando
        while tentativas > 0 and not acertou_palavra:
            limpando_terminal()

            # Mostrar o progresso do boneco
            enforcando_boneco(tentativas)

            # Progresso da palavra e dica
            print(f"\nPALAVRA SECRETA: ", end='')
            for letra in palavra_secreta:
                if letra in letras_jogadas:
                    print(letra, end=' ')
                else:
                    print("_", end=' ')
            print(f"\nDICA: {dica}")
            print(f"{jogador} está jogando\nPontos: {pontos}")
            print(f"Tentativas restantes: {tentativas}")

            # Pedindo palavra ou letra para ser adivinhada
            advinhando: str = input("\nInforme uma palavra ou letra: ").strip().lower()

            # Verificando se a letra já foi jogada
            if advinhando in letras_jogadas:
                print("Você já jogou essa letra, tente outra.")
                time.sleep(1.5)
                continue

            # Verificando se é uma tentativa de palavra inteira
            if len(advinhando) > 1:
                if advinhando == palavra_secreta:
                    print(f">>> {jogador} acertou a palavra <<<")
                    acertou_palavra = True
                    break
                else:
                    print(f">>> {jogador} errou a palavra <<<")
                    jogadores[jogador] -= 20  # Penalidade por errar a palavra
                    tentativas -= 1
                    time.sleep(1.5)
                    continue

            # Adicionando a letra ao registro de jogadas
            letras_jogadas.append(advinhando)

            # Verificando se a letra não está na palavra
            if advinhando not in palavra_secreta:
                print(f">>> A letra '{advinhando}' não está na palavra <<<")
                jogadores[jogador] -= diminuindo_pontos  # Reduz pontos por erro
                tentativas -= 1
                time.sleep(1.5)
            else:
                print(f">>> A letra '{advinhando}' está na palavra! <<<")
                time.sleep(1.5)

        if not acertou_palavra and tentativas == 0:
            enforcando_boneco(0)  # Mostra o boneco completo se perdeu

    lideres()  # Chama o ranking ao final do jogo

# Progresso da morte da VITIMA
def enforcando_boneco(tentativas: int) -> None:
    print("\n>>> PROGRESSO DO BONECO <<<")
    match tentativas:
        case 6:
            print("|-----|\n|     O\n|\n|\n|\n")
        case 5:
            print("|-----|\n|     O\n|     |\n|\n|\n")
        case 4:
            print("|-----|\n|     O\n|    /|\n|\n|\n")
        case 3:
            print("|-----|\n|     O\n|    /|\\\n|\n|\n")
        case 2:
            print("|-----|\n|     O\n|    /|\\\n|    /\n|\n")
        case 1:
            print("|-----|\n|     O\n|    /|\\\n|    / \\\n|\n")
        case 0:
            print("|-----|\n|     X\n|    /|\\\n|    / \\\n|\n")
            print("!!! VITIMA MORTA !!!")

# Exibindo o ranking dos jogadores
def lideres() -> None:
    limpando_terminal()

    # Ordena jogadores por pontos em ordem decrescente
    ranking: typing.List[typing.Tuple[str, int]] = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

    empate: bool = False
    maior_pontuacao: int = -1
    vencedor: typing.Optional[str] = None

    for jogador, pontos in ranking:
        if jogador == next(iter(jogadores)):
            continue

        print(f"{jogador} com {pontos} pontos")

        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
            vencedor = jogador
            empate = False
        elif pontos == maior_pontuacao:
            empate = True

    if empate:
        print("\n>>> HOUVE UM EMPATE <<<")
    else:
        print(f"\n>>> O VENCEDOR FOI {vencedor} <<<")

    exit()

# Dicionário de jogadores
jogadores: typing.Dict[str, int] = {}

if __name__ == "__main__":
    main()
