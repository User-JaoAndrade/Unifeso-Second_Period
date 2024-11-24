""" Passo a passo desse exercício
    1 - Pedir ao usuário uma cadeia de caracteres de no máximo 1000 caracteres
    2 - Verificar as 2 letras que mais se repetiram
    3 - a porcentagem da letra em 2 casas decimais
    4 - Se houver empate, mostrar APENAS a letra que vem primeiro na ordem alfabetica
    ps: Desconsiderar da porcentagem caracteres que não sejam de A até Z, desconsiderar
        diferenças de maiuscula ou minuscula"""

import time
import os
from collections import Counter

def limpando_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que verifica as letras mais repetidas
def calculando_letras() -> None:
    contando_letras = Counter(cadeia_de_caracteres) # Contando o número de vezes que apareceu cada letra
    numero_total_de_letras: int = sum(contando_letras.values()) # Somando todas as letras
    as_mais_brabas = contando_letras.most_common(2) # as duas que mais apareceram

    # Caso as letras tenham aparecido a mesma quantidade de
    if as_mais_brabas[0][1] == as_mais_brabas[1][1]:
        as_mais_brabas = sorted(as_mais_brabas) # Deixando em ordem alfabética

        for letra, contagem in as_mais_brabas:
            print(f"{letra.upper()}: {(contagem/numero_total_de_letras)*100:.2f}%")

    # Caso tenha um empate entre a segunda e a terceira letra que mais apareceram
    elif contando_letras[1] == contando_letras[2]:
        for letra, contagem in as_mais_brabas:
            print(f"{letra.upper()}: {(contagem/numero_total_de_letras)*100:.2f}")
            break

    else:
        for letra, contagem in as_mais_brabas:
            print(f"{letra.upper()}: {(contagem/numero_total_de_letras)*100:.2f}%")


""" inicio do programa """
if __name__ == "__main__":
    while True:
        limpando_terminal()
        cadeia_de_caracteres: str = input("Informe uma sequência de caracteres (não coloque espaços): ").lower()

        # Verificando se a cadeia de letras possui <= 1000 caracteres e se tem espaços
        if len(cadeia_de_caracteres) > 1000 or ' ' in cadeia_de_caracteres:
            print("\nPor favor, informe uma lista com:\n"
                  "- No Máximo 1000 caracteres\n" 
                  "- Sem espaços")
            time.sleep(5)
            continue

        # Removendo caracteres que não sejam de A até Z
        cadeia_de_caracteres = filter(lambda c: c.isalpha() and c.isascii(), cadeia_de_caracteres)
        

        calculando_letras()
        break