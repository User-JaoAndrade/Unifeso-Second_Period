"""Passo a passo pra saber se um número é de kaprekar
    - Eleve o numero ao quadrado
    - Divida o resultado em duas partes por exemplo 3025 = 30, 25
    - Some as duas partes
    - Verifique se a soma é igual ao numero original
"""
import time
import os

def limpando_terminal()-> None:
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print(">> NÚMERO DE KAPREKAR <<")
    while True:
        try:
            numero: int = int(input("\nInforme um número de ate 2 digitos ->  "))
            str_numero = str(numero) # Convertendo o número para uma string
            break
        except ValueError:
            print("informe um número inteiro")
            time.sleep(3)
    
    # Dividindo a string em 2 partes

    # MEXER NESSA LOGICA DEPOIS, SE EU COLOCAR 88209 E USAR A PRIMEIRA DIVISÃO ELE RETORNA 1,
    # MAS SE USAR A SEGUNDA ELE RETORNA 0
    ponto_de_divisao: int = len(str_numero) // 2 # A primeira metade é menor
    ponto_de_divisao: int = (len(str_numero)+1) // 2 # A primeira metade é maior

    primeira_metade_num: str = str_numero[:ponto_de_divisao] 
    segunda_metade_num: str = str_numero[ponto_de_divisao:]

    num_kaprekar: int = (int(primeira_metade_num) + int(segunda_metade_num)) **2

    if num_kaprekar == numero:
        print(1)
    else: 
        print(0)