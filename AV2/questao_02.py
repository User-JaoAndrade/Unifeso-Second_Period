"""Passo a passo pra saber se um número é de kaprekar
    - Eleve o numero ao quadrado
    - Divida o resultado em duas partes
    ps: a parte da direita precisa ter a mesma quantidade de digitos que o numero original
        e a parte esquerda o resto dos digitos
        por exemplo: 297 -> 297^2 -> 88209 -> 88 + 209
    - Some as duas partes
    - Verifique se a soma é igual ao numero original
"""
import time

if __name__ == "__main__":
    while True:
        print(">> NÚMERO DE KAPREKAR <<")
        try:
            numero: int = int(input("\nInforme um número de até 2 dígitos ->  "))

            # Verificando se o número é valido
            if numero < 1 or numero > 100000000:
                print("Número inválido, informe um número válido")
                time.sleep(3)
                continue

            # Convertendo o número para uma string
            str_numero = str(numero)
            break

        except ValueError:
            print("Informe um número inteiro.")
            time.sleep(1)

    string_numero: str = str(numero) # número convertido pra uma string
    diminuir_string: int = len(string_numero) - 1

    while diminuir_string > 0:
        esquerda_string: str = string_numero[:-diminuir_string] # parte esquerda
        direita_string: str = string_numero[-diminuir_string:] # parte direita

        kaprekar: int = (int(esquerda_string) + int(direita_string)) ** 2 # Calculo de Kaprekar

        # Verificando se é um número de kaprekar
        if kaprekar == numero:
            print(1)
            exit()
        else:
            diminuir_string-=1 # decrementa em 1 o tamanho da string

    print(0)
    exit()