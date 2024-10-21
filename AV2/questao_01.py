# Conjectura de Goldbach

import os
import time
from sympy import isprime # Biblioteca que vai verificar se o número é primo

# Função que limpa o terminal
def limpando_terminal()-> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função inutil de animar pontos
def animacao_pontinhos(n):
    for i in range(n):
        print('.', end='')
        time.sleep(1)

# Função inicial
def main()-> None:    
    while True:
        limpando_terminal()
        print(">> CONJUCTURA DE GOLDBACH <<")
        print('"Todo número par maior que 2 pode ser expresso como a soma de dois números primos."\n'
              '-Christian Goldbach')
        
        try:
            number: int = int(input("\nInforme um número inteiro: "))
        except ValueError:
            print("Por favor, informe um número inteiro", end='')
            animacao_pontinhos(3)
            continue

        # Verificando se o número é par
        if not number % 2 == 0 or number < 4 or number >= 4294967294:
            print("\nATENÇÃO: Possíveis erros\n"
                  " - Número não é par\n"
                  " - Número é menor que 4\n"
                  " - Número é maior que 4294967294")
            animacao_pontinhos(6)
            continue
        
        # Verificando os numeros primos que somam "number"
        for i in range(2, number):
            if isprime(i) and isprime(number - i):
                print("\n>>> RESULTADO <<<")
                print (f"{number} = {i} + {number - i}")
                break
        else:
            print("\n-1")
            break
        

        var_selecao = input("\n[1] Tentar outro número\n"
                              "[outra tecla] SAIR\n"
                              "-> ")
        
        match var_selecao:
            case '1':
                continue
            case _:
                break

if __name__ == "__main__":
    main()