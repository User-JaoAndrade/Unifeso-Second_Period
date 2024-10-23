# Neste problema, você terá acesso aos registros de banco de dados referentes ao acervo
# de livros e membros de uma biblioteca pertencente à uma instituição de ensino. Cada
# livro é composto por um título, lista de autores, edição, e quantidade de exemplares
# disponíveis na biblioteca. Implemente as funcionalidades de locação e entrega de
# exemplares do programa. Atente-se que, durante o processo de locação, é registrado a
# matrícula do membro da biblioteca que está alocando o livro, o dia da locação e o dia da
# devolução, 15 dias corridos após a data de locação. Já no processo de devolução,
# implemente as funcionalidades de verificação do título do livro devolvido, existência de
# atraso e a reposição das quantidades alocadas. Caso haja atraso na entrega, o membro
# deverá ser multado em R$ 10,00 por dia de atraso. Membros não pertencentes à
# instituição não podem alocar livros. Por fim, dê a opção do usuário do sistema informar
# uma data de início e fim para obter um relatório das alocações, devoluções, quantidades
# de atrasos e o total em reais pago em multas por cada membro.
# Dicas: (i) considere utilizar classes, listas e dicionários; (ii) utilize o método DictReader
# do módulo csv do Python para ler os registros dos arquivos. Os arquivos .csv estão
# disponíveis para download em https://bit.ly/3ZAX962.

import os
import time
import pandas as pd 
from pandas import DataFrame
import datetime as dt
import random


# função que limpa o terminal
def limpando_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


# Função Menu
def main()-> None:
    while True:
        limpando_terminal()
        # Ajustando as configurações para exibir todas as linhas e colunas
        pd.set_option('display.max_rows', None)  # Exibe todas as linhas
        pd.set_option('display.max_columns', None)  # Exibe todas as colunas
        pd.set_option('display.width', 1000)  # Largura máxima da saída
        pd.set_option('display.expand_frame_repr', False)  # Não quebra linhas

        print(f"HOJE É DIA: {dia_de_hoje}\n")
        print(":) |BIBLIOTECA TOMA LEITURA| (:\n")
        var_selecao: str = input("[1] Lista de Livros\n"
                                "[2] Informações de TODOS os membros\n"
                                "[3] Alugar Livro\n"
                                "[4] Devolução\n\n"
                                "[outra tecla] SAIR\n\n"
                                "--> ")
        match var_selecao:
            # Caso o usuário queira ver a lista de livros e seu estoque
            case '1':
                limpando_terminal()
                print(livros_df)
                input("\naperte ENTER para voltar ao menu...")

            # Caso o usuário queira ver a lista de membros
            case '2':
                limpando_terminal()
                print(membros_df)
                input("\naperte ENTER para voltar ao menu...")

            # Caso o usuário queira alugar um livro
            case '3':
                aluguel_de_livro()

            # Caso o usuário queira devolver um livro
            case '4':
                devolucao_do_livro()

            # Caso o usuário queira sair do programa
            case _:
                exit()

# Função para alugar livros
def aluguel_de_livro() -> None:
    limpando_terminal()
    print(">>>> ALUGUEL DE LIVRO <<<<\n")
    nome_livro: str = input("Informe o nome do livro que deseja alugar \n"
                            "(por favor, escreva exatamente como está na tabela)\n\n"
                            "-> ")
    
    # Verificando se o livro existe no banco de dados
    if nome_livro in livros_df['Título'].values:

        # Colocando os valores da linha na variavel
        row_livro = livros_df.loc[livros_df['Título'] == nome_livro]
        
        if row_livro['Quantidade'].iloc[0] == 0:
            print(f"\n{row_livro['Título'].iloc[0]} não está disponivel para aluguel, volte outro dia :D\n")
            input("Aperte ENTER para voltar ao menu...")
            main()
            
        # Verificando a matrícula do usuário
        while True:
            limpando_terminal()
            print(">>> INFORMAÇÕES SOBRE O LIVRO <<<\n")
            print(f"Livro encontrado: {row_livro['Título'].iloc[0]}\n"
                f"Edição: {row_livro['Edição'].iloc[0]}\n"
                f"Autor: {row_livro['Autores'].iloc[0]}\n"
                f"Quantidade em estoque: {row_livro['Quantidade'].iloc[0]}\n")
            
            # Verificando se o tem o livro em estoque
            if row_livro['Quantidade'].iloc[0] == 0:
                print(f"\nEstoque de {row_livro['Título'].iloc[0]} zerado")
                input("APERTE ENTER PARA VOLTAR AO MENU...")
                main()
            
            print("| Agora nos envie alguns dados para finalizar o aluguel de seu livro |\n")
            # Pedindo o número de matricula
            user_matricula: str = input("MATRÍCULA\n"
                                            "Informe seu número de matrícula\n"
                                            "-> ")
            
            # Caso o usuário já tenha alugado um livro
            if user_matricula in relatorios.keys():
                limpando_terminal
                print(f"\n>> ATENÇÃO <<\n{user_matricula} já alugou um livro, devolva o livro anterior antes de alugar um novo!")
                input("\nPressione ENTER para voltar ao menu...")
                main()
            
            # Verificando se o número de matrícula está no banco de dados
            while user_matricula not in membros_df['Matrícula'].values:
                var_opcao: str = input("\nNÚMERO DE MATRÍCULA NÃO ENCONTRADO, apenas membros podem alugar um livro\n"
                                    "deseja tentar novamente?\n\n"
                                    "[1] Sim\n"
                                    "[outra tecla] Não\n\n"
                                    "-> ")
                match var_opcao:
                    case '1':
                        break
                    case _:
                        main()
            # Caso o número de Matricula esteja no banco de dados
            else:
                row_membros = membros_df.loc[membros_df['Matrícula'] == user_matricula]
                break
    
    # Caso o livro não Exista no banco de dados
    else: 
        var_opcao: str = input(f"\n'{nome_livro}' NÃO FOI ENCONTRADO, deseja tentar novamente?\n\n"
                               "[1] Sim\n"
                               "[outro valor] Não\n\n"
                               "-> ")
        match var_opcao:
            case '1': 
                aluguel_de_livro()
            case _:
                main()
    
    data_de_entrega = dia_de_hoje + dt.timedelta(days=15) # Criando a data de entrega
    
    limpando_terminal()
    print("\n>>> INFORMAÇÕES SOBRE O ALUGUEL <<<\n")
    print(f"Usuário: {row_membros['Matrícula'].iloc[0]} - {row_membros['Nome'].iloc[0]}\n"
          f"Nome do Livro: {row_livro['Título'].iloc[0]}\n"
          f"Alugado dia: {dia_de_hoje}\n"
          f"Data de Entrega: {data_de_entrega}\n"
          f"Será cobrado R$10,00 por cada dia de atraso na entrega")
    
    # Diminuindo a quantidade de livros no csv
    livros_df.loc[livros_df['Título'] == nome_livro, 'Quantidade'] -= 1

    # Adicionando informações ao relatorio
    relatorios[user_matricula] = [data_de_entrega, row_membros['Nome'].iloc[0], nome_livro]  
    #                                   1                       2                   3     

    # linhas pra deixar o códico fofo
    print("\n\no/ entregando livro", end='')
    for i in '...':
        print(i, end='')
        time.sleep(1)
    input("\n\naperte ENTER para voltar ao menu...")
    main()

# Função para devolver o livro
def devolucao_do_livro() -> None:
    limpando_terminal()
    print(">>> DEVOLUÇÃO DO LIVRO <<<\n")

    # Verificando se o dicionário está vazio
    if not relatorios:
        print("\nHISTÓRICO DE ALUGUEIS VAZIO")
        input("Aperte ENTER para continuar...")
        return
    
    # Pedindo número de matrícula ao usuário
    numero_matricula: str = input("Nos informe seu número de matricula: ")

    # Verificando se o número de matrícula está no Banco de dados
    if numero_matricula not in membros_df["Matrícula"].values:
        var_selecao: str = input("\nMEMBRO NÃO ENCONTRADO\n"
                                 "Gostaria de tentar novamente?\n"
                                 "[1] Sim\n"
                                 "[outra tecla] Não\n\n"
                                 "-> ")
        match var_selecao:
            case '1':
                devolucao_do_livro()
            case _:
                main()
    
    # Verificando livro para ser devolvido
    nome_livro: str = input("\n>> Informe o livro para ser devolvido <<\n"
                            "-> ")

    # Verificando se o livro é o mesmo que foi alugado
    while nome_livro != relatorios[numero_matricula][2]:
        nome_livro = input("\nVOCÊ NÃO ALUGOU ESSE LIVRO\n"
              "informe o livro que alugou: ")
        
    # Pedindo a data de entrega do livro
    while True:
        print("\n>> Informe o dia que está devolvendo o livro <<\n")
        try:
            dia: int = int(input("Dia: "))
            mes: int = int(input("Mês: "))
            ano: int = int(input("Ano: "))
            dia_da_entrega = dt.date(ano, mes, dia)
            dias_passados: int = (dia_da_entrega - dia_de_hoje).days

            # Verificando se a data informada antecede a data que foi recebido o livro
            if dia_da_entrega < dia_de_hoje:
                print(f"\n\nViajante do tempo amigo? Informe uma data após ou igual ao dia {dia_de_hoje}")
                continue
            else: 
                break

        except ValueError:
            print("Por favor, informe uma data válida\n")
            time.sleep(3)
    
    # calculando possivel multa

    # Verificando se existe atraso
    if dias_passados > 15:
        multa: float = (dias_passados - 15) * 10 # Calculando valor da multa
        dias_passados =  dias_passados - 15
    else:
        multa: float = 0
        dias_passados = 0
 
    # Mostrando informações sobre a devolução
    print("\nCalculando possível multa", end='')
    for i in '....':
        print(i, end='')
        time.sleep(1)

    limpando_terminal()

    print(">> INFORMAÇÕES SOBRE A DEVOLUÇÃO <<\n\n"
          f"Membro: {relatorios[numero_matricula][1]}\n"
          f"Livro Alugado: {relatorios[numero_matricula][2]}\n"
          f"Data de Aquisição: {dia_de_hoje}\n"
          f"Data para ser Devolvido: {relatorios[numero_matricula][0]}\n"
          f"Data que foi entregue para biblioteca: {dia_da_entrega}\n"
          f"Dias de atraso: {dias_passados}\n"
          f"Multa a ser paga: R${multa}")
    
    # Linhas de código pra deixar o programa mais fofinho
    if multa > 0:
        print("\nPagando a multa", end='')
        for i in '...':
            print(i, end='')
            time.sleep(1)
        membros_df.loc[membros_df['Matrícula'] == numero_matricula, 'Atrasos'] += 1 # Adicionando um atraso ao histórico do usuario
        membros_df.loc[membros_df['Matrícula'] == numero_matricula, 'Multas'] += multa # Incrementando valor da multa no histórico do usuario

    print(f"\nColocando '{nome_livro}' na prateleira", end='')
    for i in '...':
        print(i, end='')
        time.sleep(1)

    # Realocando o livro na biblioteca
    livros_df.loc[livros_df["Título"] == nome_livro, 'Quantidade'] += 1 

    # Removendo informações do aluguel
    relatorios.pop(numero_matricula)

    input("\n\nAperte ENTER para voltar ao menu...")
    
    

# INICIO DO PROGRAMA
if __name__ == "__main__":
    # Criando uma variável com os dados no arquivo "livros.csv"
    livros_df: DataFrame = pd.read_csv("livros.csv", dtype={
        'Título': str,
        'Autores': str,
        'Edição': int,
        'Quantidade': int
    })
        
    # Criando uma variável com os dados no arquivo "membros.csv"
    membros_df: DataFrame = pd.read_csv("membros.csv", dtype={
        'Matrícula': str,
        'Nome': str
    })

    membros_df['Atrasos'] = [random.randint(0, 5) for _ in range(len(membros_df))]  # Adicionando uma coluna para mostrar a quantidade de atrasos que um usuário possui
    membros_df['Multas'] = [random.randint(0, 10)*10 for _ in range(len(membros_df))] # Adicionandno uma coluna para mostrar a quantidade total de multas pagas

    # Dicionario com o relatório de casa usuário
    relatorios = {}

    # Data atual do dispositivo
    dia_de_hoje = dt.date.today()

    main()