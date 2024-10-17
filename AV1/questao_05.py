'''Crie um programa que simule um sistema de votação eletrônica. O programa deve
permitir o cadastro de candidatos e eleitores, registrar votos (considerando a
possibilidade de votos nulos e brancos) e gerar um relatório final com os resultados.
Implemente funções para verificar a elegibilidade dos eleitores e evitar votos duplicados
(i.e. impedir a tentativa de um mesmo eleitor votar duas vezes). Dica: utilize dicionários
para agilizar as operações de registros e análises de votos, como também a verificação
de registros de votos duplicados.'''

import os
import time
import random
from typing import Dict, List, Tuple, Union

def limpar_linhas(n: int) -> None:
    for _ in range(n):
        print("\033[F\033[K", end='')

def limpando_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Dicionários com candidatos e eleitores
lista_candidatos: Dict[str, List[Union[str, int]]] = {
    '31': ['Polvo', 60, 0],  # numero de candidato: [nome, idade, votos]
    '71': ['Biroliro', 62, 0],
}

nulos_brancos: Dict[str, List[Union[str, int]]] = {
    '11': ['NULO', 0],
    '22': ['BRANCO', 0]
}

lista_eleitores: Dict[str, List[Union[str, str, int, bool]]] = {}  # CPF:[nome, nacionalidade, idade, votou ou não]

def main() -> None:
    while True:
        limpando_terminal()

        print(" >>> MENU DO CAIXA ELEITORAL JJLR <<<")
        print("\n[1] Cadastrar Eleitor\n[2] Cadastrar Candidato\n[3] Lista de eleitores e candidatos\n\n[4] Iniciar votação\n[5] Finalizar votação e ver os vencedores\n\n[outro] SAIR DO PROGRAMA\n")
        selecionar_opcao = input("---> ")

        match selecionar_opcao:
            case '1':
                cadastrar_eleitores()
            case '2':
                cadastrar_candidatos()
            case '3':
                todos_os_candidatos_e_eleitores()
            case '4':
                votacao()
            case '5':
                verificando_vencedores()
            case _:
                exit()

# Função de cadastro dos eleitores '1'
def cadastrar_eleitores() -> None:
    limpando_terminal()

    print(">>> CADASTRANDO ELEITOR <<<"
          "\n Nos informe:"
          "\n -Seu CPF"
          "\n -Nome"
          "\n -Nacionalidade"
          "\n -Idade\n")

    cpf: str = input("Informe seu CPF\n  -Seu CPF precisa ter 11 dígitos\n---> ")
    while cpf in lista_eleitores.keys() or len(cpf) != 11 or ' ' in cpf:
        cpf = input("\n> ERRO AO CADASTRAR CPF <"
                    "\nPossiveis erros"
                    "\n  -O CPF informado já foi cadastrado"
                    "\n  -O CPF informado não possui 11 dígitos"
                    "\n  -O CPF informado possui espaço\n\n--> ")

    nome: str = input("Informe seu nome: ")
    nacionalidade: str = input("Nacionalidade: ")

    while True:
        try:
            idade: int = int(input("Informe sua idade: "))
            if idade < 18:
                print("IDADE INVÁLIDA, VOLTE QUANDO POSSUIR 18 ANOS")
                for letra in "retornando":
                    print(letra, end='')
                    time.sleep(0.3)
                return
            else: 
                break
        except ValueError:
            print("POR FAVOR, INFORME UM NÚMERO")
            for letra in 'retornando':
                print(letra, end='')
                time.sleep(0.3)

    lista_eleitores[cpf] = [nome, nacionalidade, idade, False]
    
    print("\n>> CADASTRO DE ELEITOR REALIZADA COM SUCESSO <<")
    for letra in "retornando":
        print(letra, end='')
        time.sleep(0.3)

# Função de cadastro dos candidatos '2'
def cadastrar_candidatos() -> None:
    limpando_terminal()
    print(" >>>> CADASTRANDO CANDIDATO <<<<"
          "\nNos informe:"
          "\n -Seu Código de candidato"
          "\n -Seu nome"
          "\n -Idade\n")
    
    codigo: str = input("Informe seu código: ")
    while codigo in lista_candidatos.keys():
        print("\n> CODIGO JÁ UTILIZADO <\n")
        codigo = input("Informe outro código: ")
    
    nome: str = input("Informe seu nome: ")

    while True:
        try:
            idade: int = int(input("Informe sua idade: "))
            if idade < 18:
                print("IDADE INVÁLIDA, VOLTE QUANDO POSSUIR 18 ANOS")
                for letra in "retornando":
                    print(letra, end='')
                    time.sleep(0.3)
                return
            else: 
                break
        except ValueError:
            print("POR FAVOR, INFORME UM NÚMERO")
            for letra in 'retornando':
                print(letra, end='')
                time.sleep(0.3)

    lista_candidatos[codigo] = [nome, idade, 0]

    print("\n>> CADASTRO DE CANDIDATO REALIZADO COM SUCESSO <<")
    for letra in "retornando":
        print(letra, end='')
        time.sleep(0.3)

# Função para mostrar todos os cadastros '3'
def todos_os_candidatos_e_eleitores() -> None:
    limpando_terminal()
    print(">>> LISTA DE CANDIDATOS E ELEITORES <<<")

    print("ELEITORES\n", "-" * 30)
    for cpf, (nome, nacionalidade, idade, votou) in lista_eleitores.items():
        print(
            "\n".join([ 
                f"Nome: {nome}",
                f"CPF: {cpf}",
                f"Idade: {idade}",
                f"Nacionalidade: {nacionalidade}",
                f"Votou: {'Sim' if votou else 'Não'}",
                ""])
        )
        print("_" * 30)
    
    print("\nCANDIDATOS\n", "-" * 30)
    for numero_candidato, (nome, idade, votos) in lista_candidatos.items():
        print(
            "\n".join([
                f"Número do Candidato: {numero_candidato}",
                f"Nome: {nome}",
                f"IDADE: {idade}",
            ])
        )
        print("_" * 30)
        
    input("Aperte ENTER para voltar ao menu...")

# Função de votação '4'
def votacao() -> None:
    limpando_terminal()
    
    print(">>> VOTAÇÃO <<<"
        "\n Iremos verificar"
        "\n -Seu CPF"
        "\n -Se já votou ou não\n")
    
    cpf: str = input("Informe seu cpf: ")
    while cpf not in lista_eleitores.keys() or len(cpf) != 11 or ' ' in cpf:
        cpf = input("CPF não encontrado, informe outro: ")

    print("Verificando se o usuário já votou", end="")
    for letra in "...":
        print(letra, end='')
        time.sleep(0.75)

    if lista_eleitores[cpf][3]:
        print(f"\n{lista_eleitores[cpf][0]} já votou")
        for letra in "retornando":
            print(letra, end='')
            time.sleep(0.3)
        return
    
    print("\n\nCANDIDATOS\n", "-" * 30)
    for numero_candidato, (nome, idade, _) in lista_candidatos.items():
        print(
            "\n".join([
                f"Número do Candidato: {numero_candidato}",
                f"Nome: {nome}",
                f"IDADE: {idade}",
            ])
        )
        print("_" * 30)

    print("11 - NULO")
    print("22 - BRANCO")
    
    voto: str = input("\nInforme o número do seu candidato (ou 11 para NULO, 22 para BRANCO): ")
    
    if voto in lista_candidatos.keys():
        lista_candidatos[voto][2] += 1  # Acrescenta 1 a contagem de votos do candidato
    elif voto == '11':
        nulos_brancos['11'][1] += 1  # Incrementa votos nulos
    elif voto == '22':
        nulos_brancos['22'][1] += 1  # Incrementa votos em branco
    else:
        print("\nCANDIDATO NÃO ENCONTRADO, voto não contabilizado.")
    
    lista_eleitores[cpf][3] = True  # Carimbando que o usuário já votou

# Contando os votos
def verificando_vencedores() -> None: 
    # Adicionando votos aleatórios
    for _ in range(200):
        # Seleciona um número aleatório entre 1 e 100
        voto_aleatorio: int = random.randint(1, 100)
        
        # Com 70% de chance de votar em um candidato
        if voto_aleatorio <= 70:
            numero_candidato: str = random.choice(list(lista_candidatos.keys()))
            lista_candidatos[numero_candidato][2] += 1
        # Com 20% de chance de votar nulo
        elif voto_aleatorio <= 90:
            nulos_brancos['11'][1] += 1
        # Com 10% de chance de votar em branco
        else:
            nulos_brancos['22'][1] += 1

    limpando_terminal()
    print(">>> CONTANDO VOTOS E MOSTRANDO O VENCEDOR <<<")
    for letra in "...":
        print(letra, end='')
        time.sleep(1)

    mais_votado: Union[str, None] = None
    maiores_votos: int = -1
    empate: bool = False

    for _, (nome, _, votos) in lista_candidatos.items():
        if maiores_votos < votos:
            mais_votado = nome
            maiores_votos = votos
            empate = False
        elif maiores_votos == votos:
            empate = True

    if empate: 
        print("\n>>>> Houve um empate <<<<")
    else:
        print(f"\n>>>> O NOVO IMPERADOR É O {mais_votado} com {maiores_votos} votos <<<<")
    
    # Exibindo resultados de nulos e brancos
    print(f"\nVotos Nulos: {nulos_brancos['11'][1]}")
    print(f"Votos em Branco: {nulos_brancos['22'][1]}")
    exit()

if __name__ == "__main__":
    main()
