'''Crie um programa que simule um jogo de adivinhação de palavras. O programa deve
escolher aleatoriamente uma palavra de uma lista predefinida e dar ao usuário um
número limitado de tentativas para adivinhar. Após cada tentativa, o programa deve
informar quais letras estão corretas e em posição correta, e quais estão corretas mas em
posição errada. Implemente uma função para gerar dicas baseadas nas tentativas
anteriores do usuário.'''

import os
import random
import time
from typing import Dict

def main() -> None:
    # listas
    lista_palavras: Dict[str, list[str]] = {
        'cachorro': [
            "Relação com o ser humano",
            "Habilidades especiais",
            "Companhia leal",
            "Latidos característicos"
        ],

        'chocolate': [
            "Combinações em sobremesas",
            "Emoções de prazer",
            "Sabor doce e amargo",
            "Origem do cacau"
        ],

        'futebol': [
            "Originado na Inglaterra",
            "Esporte com bola",
            "Dois times competindo",
            "Cada time tem 11 jogadores"
        ],

        'programador': [
            "Resolve problemas",
            "Lógica é essencial",
            "Trabalha com diversas linguagens",
            "Escreve código"
        ],

        'quimera': [
            "Criatura mítica da mitologia grega",
            "Mistura de várias partes de animais",
            "Simboliza um sonho irrealizável",
            "Associada a fogo e destruição"
        ],

        'serendipidade': [
            "Descobertas felizes por acaso",
            "Encontrar algo inesperado",
            "Associada a inovações",
            "Vem de um conto persa"
        ],

        'epifania': [
            "Momento de súbita revelação",
            "Compreensão em situações cotidianas",
            "Experiência iluminadora",
            "Mudança de perspectiva"
        ],

        'cacofonia': [
            "Combinação de sons desagradáveis",
            "Usada em poesia e retórica",
            "Oposto de eufonia",
            "Barulho intenso e confuso"
        ],

        'anacronismo': [
            "Algo fora de seu tempo cronológico",
            "Encontrado em filmes históricos",
            "Refere-se a objetos ultrapassados",
            "Crítica a algo antiquado"
        ],

        'paradoxo': [
            "Declaração que contradiz a lógica",
            "Apresenta uma verdade oculta",
            "Usado em filosofia",
            "Desafia a intuição"
        ]
    }

    PALAVRA_SECRETA: str = random.choice(list(lista_palavras.keys()))
    menu_de_jogo(PALAVRA_SECRETA, lista_palavras)

'''>>>Função do jogo<<<'''
def menu_de_jogo(PALAVRA_SECRETA: str, lista_palavras: Dict[str, list[str]]) -> None:
    advinhando_palavra: str = ''
    tentativas: int = 5
    os.system('cls' if os.name == 'nt' else 'clear')

    print(">>> JOGO DA PALAVRA SECRETA <<<\n")
    print("Vamos jogar um jogo?")
    gameplay(PALAVRA_SECRETA, advinhando_palavra, tentativas, lista_palavras)

def gameplay(PALAVRA_SECRETA: str, advinhando_palavra: str, tentativas: int, lista_palavras: Dict[str, list[str]]) -> None:
    j: int = 0
    formando_palavra: str = ''

    while tentativas > 0:
        print(f"\nA palavra secreta possui {len(PALAVRA_SECRETA)} letras")
        print(f"Tentativas restantes {tentativas}")
        advinhando_palavra = input("Diga uma palavra: ").lower()
        print("\n", end='')
        
        # Verificando se acertou a palavra
        if advinhando_palavra == PALAVRA_SECRETA:
            print(f"\n>>> PARABÉNS, VOCÊ ACERTOU A PALAVRA SECRETA ({PALAVRA_SECRETA}) EM {5 - tentativas} tentativas <<<\n")
            advinhando_palavra = input("Deseja jogar novamente?\n[1] Sim\n[outra tecla] Não\n\n---> ")
            if advinhando_palavra == '1':
                main()
            else:           
                break 
        # verificando letra por letra se estão na palavra
        else:
            for i in range(len(advinhando_palavra)):
                # Se ainda estiver dentro do tamanho da palavra secreta
                if i < len(PALAVRA_SECRETA):

                    # Se a letra adivinhada está na mesma posição que na palavra secreta
                    if advinhando_palavra[i] == PALAVRA_SECRETA[i]:
                        print(f'"{advinhando_palavra[i].upper()}" está na palavra secreta e na posição correta')
                        formando_palavra += advinhando_palavra[i]  

                    # Se a letra existe na palavra secreta, mas em outra posição
                    elif advinhando_palavra[i] in PALAVRA_SECRETA:
                        print(f'"{advinhando_palavra[i].upper()}" na palavra mas na posição errada')
                        formando_palavra += '*' 
                    
                    # Letra não existe na palavra secreta
                    else:
                        print(f'"{advinhando_palavra[i]}" não está na palavra')
                        formando_palavra += '*'  
                
                # Se a letra está além do tamanho da palavra secreta
                else:
                    formando_palavra += '*'  # Se a letra está além do tamanho da palavra secreta
        
        dicas(PALAVRA_SECRETA, lista_palavras, j)
        j += 1
        tentativas -= 1
                
    

    print(f"\n\n!!! VOCÊ PERDEU !!!\nA palavra secreta era '{PALAVRA_SECRETA}'\n\n")
    advinhando_palavra = input("Deseja jogar novamente?\n[1] Sim [outra tecla] Não\n---> ")

    if advinhando_palavra == '1':
        main()
    else: 
        print("\nOBRIGADO POR JOGAR")
        time.sleep(3)
        exit()

def dicas(PALAVRA_SECRETA: str, lista_palavras: Dict[str, list[str]], i: int) -> None:
    if i < len(lista_palavras[PALAVRA_SECRETA]):
        print(f"\n>>> DICA: {lista_palavras[PALAVRA_SECRETA][i]}")

if __name__ == '__main__':
    main()
