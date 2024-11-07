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

while True:
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

    numero_ao_quadrado: int = numero ** 2 # Elevando o número original ao quadrado
    str_numero_ao_quadrado = str(numero_ao_quadrado)

    # Dividindo o número ao quadrado em duas partes
    parte_direita = str_numero_ao_quadrado[-len(str_numero):]  # Últimos 'tamanho_num_original' dígitos
    parte_esquerda = str_numero_ao_quadrado[:-len(str_numero)] or "0"  # O restante (se não houver, coloca 0)
    
    if parte_esquerda == '':
        parte_esquerda = '0'

    # Calculando a soma das duas partes
    num_kaprekar = int(parte_esquerda) + int(parte_direita)

    # Verificando se o número é de Kaprekar
    if num_kaprekar == numero:
        print(1)
    else:
        print(0)