"""
Mostrar apenas mensagens com frequencias > 100 por exemplo:
-> 100oj85iu101bat76hjhj188at87oi102a
saida = batata

simbolos são consideras interferencia
"""

import time

# Função de animação inutil
def print_animation(phrase, timer)-> None:
    for letter in phrase:
        print(letter, end='')
        time.sleep(timer)

# inicio do programa
if __name__ == "__main__":
    print_animation(">> TRADUTOR KNI <<", 0.02)
    print_animation("\nCódigo para decodificar ->  ", 0.02)
    kni_code: str = input()

    print_animation("\ndecodificando", 0.02)
    print_animation("...", 1)
    print("\n")

    for i, caractere in enumerate(kni_code):

        # Verificando se o digito é um número
        if caractere.isdigit():
            numero:str = caractere
            j = i + 1

            # Caso o proximo indice seja um numero
            while j < len(kni_code) and kni_code[j].isdigit():
                numero += kni_code[j] # Concatenando para formar o número completo
                j+=1

            # Caso o número concatenado seja maior que 100 e menor que 200
            if int(numero) > 100 and int(numero) < 200:
                while j < len(kni_code) and not kni_code[j].isdigit():
                    # Caso seja um símbolo ele pula pro próximo indice
                    if not kni_code[j].isalpha():
                        j+=1
                        continue

                    print_animation(kni_code[j], 0.2)
                    j+=1

            i = j

    print("")