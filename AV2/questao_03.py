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

def limpando_terminal()-> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que verifica as letras mais repetidas
def calculando_letras() -> None:
    contador_de_letras = Counter(cadeia_de_caracteres)
    ...

if __name__ == "__main__":
    while True:
        limpando_terminal()
        cadeia_de_caracteres: str = input("Informe uma sequência de caracteres (não coloque espaços): ")
        
        # Verificando se a cadeia de letras possui <= 1000 caracteres e se tem espaços
        if len(cadeia_de_caracteres) > 1000 or ' ' in cadeia_de_caracteres:
            print("\nPor favor, informe um lista com:\n"
                  "- No Máximo 1000 caracteres\n" 
                  "- Sem espaços")
            time.sleep(5)
            continue

        calculando_letras()