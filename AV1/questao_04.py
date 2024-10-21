'''Desenvolva um programa que simule um caixa eletrônico de um banco com múltiplas
contas correntes. O programa deve permitir operações como depósito, saque,
transferência entre contas e consulta de extrato (o extrato deve exibir o saldo da conta,
juntamente com o registro de todas as transações efetuadas pelo cliente). Implemente
também um sistema de cadastro de senhas para cada nova conta cadastrada. Essa
senha será requerida pelo sistema ao usuário para a conclusão de uma das transações
supracitadas. No caso do usuário digitar três vezes a senha incorreta, a conta do usuário
deverá ser bloqueada e uma mensagem deverá surgir, orientando que o cliente se dirija
à boca do caixa para efetuar o desbloqueio.'''

import os
import time
from typing import Dict, List, Union

# Tipo para armazenar informações dos usuários
UserInfo = List[Union[str, float, str, List[str]]]
UserDatabase = Dict[str, UserInfo]

# Função para apagar linhas
def limpar_linhas(n: int) -> None:
    for _ in range(n):
        print("\033[F\033[K", end='')


# Função de Menu (dã)
def main() -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(">>> BANCO JJLR <<<\n")
        var_selecao = input('[1] LOGIN\n[2] CADASTRAR\n[3] BOCA DO CAIXA\n[Outra Tecla] SAIR\n\n==> ')

        match var_selecao:
            case '1':
                entrada_da_conta()
            case '2':
                cadastrando_novo_usuario()
            case '3':
                desbloqueio_de_conta()
            case _:
                exit()


# Função que vai adicionar uma nova key e valores para o dicionário
def cadastrando_novo_usuario() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(">>> CADASTRANDO NOVO CLIENTE <<<\n")

    # Pedindo um nome pro usuário
    nome_usuario = input("Informe um nome de usuario: ").lower()

    # Verificando se já existe esse usuário (key) no dicionário
    while ' ' in nome_usuario or nome_usuario in lista_de_usuarios.keys():
        limpar_linhas(1)
        nome_usuario = input("Nome de usuário já utilizado ou contém espaços, informe outro nome: ")

    # Pedindo uma senha para o usuário
    senha_usuario = input("\nInforme uma senha\nps: Sua senha precisa ter 6 digitos e não pode conter espaços\nSenha de usuário: ")

    # Verificando se a senha contém espaços e se possui 6 caracteres
    while ' ' in senha_usuario or len(senha_usuario) != 6:
        limpar_linhas(1)
        senha_usuario = input("A sua senha não contém 6 digitos ou contém espaços, informe outra senha: ")

    print("\n<<<< USUARIO CADASTRADO COM SUCESSO >>>>")
    tres_pontinhos()

    lista_de_usuarios[nome_usuario] = [senha_usuario, 0.0, 'unlocked', []] # adicionando a key e valores ao dicionário


# Função para logar na conta
def entrada_da_conta() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    # variável que vai guardar o número de tentativas ao colocar a senha
    print(" >>>> TELA DE LOGIN <<<<\n")

    # Pedindo um nome de usuário que já exista no dicionário
    login_usuario: str = input("NOME DE USUÁRIO: ")
    # Verificando se o usuário está presente no dicionário
    if login_usuario not in lista_de_usuarios.keys():
        limpar_linhas(1)
        var_selecao: str = input("Usuário não encontrado, deseja: [1] Tentar Novamente | [2] Realizar um novo cadastro | [outra tecla] Voltar ao Menu --> ")
        if var_selecao == '1':
            entrada_da_conta()
        elif var_selecao == '2':
            cadastrando_novo_usuario()
            main()
        else: 
            main()
        
    # Verificando se a conta está bloqueada
    if lista_de_usuarios[login_usuario][2] == 'locked':
        print("CONTA BLOQUEADA, VÁ ATÉ A BOCA DO CAIXA PARA REALIZAR O DESBLOQUEIO")
        print("\nRetornando", end='')
        tres_pontinhos()

    # Pedindo senha ao usuário
    senha_usuario: str = input("SENHA: ")

    verificacao_de_senha(senha_usuario, login_usuario)

    print("\nLOGANDO NA SUA CONTA", end='')
    for i in '...':
        print(i, end='')
        time.sleep(1)
    informacoes_de_usuario(login_usuario)


# Função para desbloquear uma conta
def desbloqueio_de_conta() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(">>>> DESBLOQUEIO DE CONTA <<<<\n")
    print("Para desbloquear a sua conta informe o seu nome de usuário e uma nova senha\n")
    
    # pedindo um nome de usuário presente no dicionário
    nome_usuario: str = input("Informe o usuário que deseja desbloquear: ")
    
    # verificando se o usuário está presente na lista
    while nome_usuario not in lista_de_usuarios.keys():
        limpar_linhas(1)
        nome_usuario = input("Usuário não encontrado, informe um usuário válido: ")

    # Colocando uma senha nova
    nova_senha = input("\nInforme uma nova senha\nps: Sua senha precisa ter 6 digitos e não pode conter espaços\nSenha de usuário: ")
    
    # verificando se a senha contém espaços ou se possui um tamanho diferente de 6 digitos
    while ' ' in nova_senha or len(nova_senha) != 6:
        limpar_linhas(1)
        nova_senha = input("Sua senha possui espaços ou não contém 6 digitos, por favor informe uma senha válida: ")
    
    # Verificando se a nova senha é igual a senha anterior da conta
    while nova_senha == lista_de_usuarios[nome_usuario][0]:
        limpar_linhas(1)
        nova_senha = input("Essa foi sua senha anterior, por favor informe uma nova senha: ")

    print("\n<<<< NOVA SENHA CADASTRADA COM SUCESSO >>>>")
    print("Retornando para o menu", end='')
    tres_pontinhos()
    
    lista_de_usuarios[nome_usuario][0] = nova_senha # Adicionando a nova senha
    lista_de_usuarios[nome_usuario][2] = 'unlocked' # Desbloqueando a conta


# Função que mostra as informações do usuário selecionado
def informacoes_de_usuario(login_usuario: str) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f">>> informações da {login_usuario}<<<\n")
    print(f"Saldo em conta R${lista_de_usuarios[login_usuario][1]:.2f}\n\nSelecione o que deseja fazer\n")
    var_selecao = input("[1] Depósito\n[2] Saque\n[3] Transferencia\n[4] Extrato\n[outra tecla] SAIR\n\n---> ")
    
    match var_selecao:
        case '1':
            deposito(login_usuario)
        case '2':
            saque(login_usuario)
        case'3':
            transferencia(login_usuario)
        case '4':
            extrato_bancario(login_usuario)
        case _: 
            main()


# Função para depositar 'dinheiros' na conta
def deposito(login_usuario: str) -> None:
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            print('>>>> DEPOSITO <<<<\n')
            # informando um valor para depositar
            valor_para_depositar: float = float(input("Valor que deseja depositar na sua conta: "))

        # caso o usuário não coloque um número
        except ValueError:
            print("Por favor, informe apenas números", end='')
            tres_pontinhos()
            continue

        # Pedindo senha para finalizar o deposito
        senha_usuario: str = input("SENHA: ")
        
        verificacao_de_senha(senha_usuario, login_usuario)

        lista_de_usuarios[login_usuario][1] += valor_para_depositar # Adicionando o valor selecionado
        # adiconando uma frase para ver o extrato depois
        lista_de_usuarios[login_usuario][3].append(f"+R${valor_para_depositar:.2f}")
        
        print("Valor depositado com sucesso", end='')
        tres_pontinhos()
        break

    informacoes_de_usuario(login_usuario)


# Função para retirada de dinheiro da conta 
def saque(login_usuario: str) -> None:
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            print('>>>> SAQUE <<<<\n')
            # informando o valor para retirar da conta
            valor_para_retirar: float = float(input("Valor que deseja retirar da sua conta: "))

        # caso o usuário não coloque um número
        except ValueError:
            print("Por favor, informe apenas números", end='')
            tres_pontinhos()
            continue
        
        # Verificando se o valor de retirada é maior que o saldo da conta
        if valor_para_retirar > lista_de_usuarios[login_usuario][1]:
            limpar_linhas(1)
            var_selecao: str = input("O valor de saque excede seu saldo\n[1] Colocar outro valor\n[outra tecla] Voltar para o menu\n---> ")
            if var_selecao == '1':
                continue
            else: 
                informacoes_de_usuario(login_usuario)
        
        # Pedindo senha para finalizar o deposito
        senha_usuario: str = input("SENHA: ")
        
        verificacao_de_senha(senha_usuario, login_usuario)
                
        lista_de_usuarios[login_usuario][1] -= valor_para_retirar # Subtraindo o valor informado
        
        # Adicionando uma frase para ver o extrato depois
        lista_de_usuarios[login_usuario][3].append(f"-R${valor_para_retirar:.2f}")
        
        print("Valor retirado com sucesso", end='')
        tres_pontinhos()
        break

    informacoes_de_usuario(login_usuario)


# Função para transferência de valores entre as contas
def transferencia(login_usuario: str) -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('>>>> TRANSFERÊNCIA <<<<\n')
        
        # informando o usuário que deseja transferir
        usuario_para_transferir: str = input("Informe o nome do destinatário: ").lower()

        # verificando se o usuário informado existe no dicionário
        if usuario_para_transferir not in lista_de_usuarios.keys():
            print ("\n>> Usuário não encontrado <<\n\n")
            var_selecao: str = input("Deseja tentar novamente?\n"
                                     "[1] Sim\n"
                                     "[Outra tecla] Não\n"
                                     "-> ")
            match var_selecao:
                case '1': 
                    continue
                case _:
                    informacoes_de_usuario(login_usuario)

        # Verificando se vai tentar tranferir para a própria conta
        if usuario_para_transferir == login_usuario:
            print("\n>>> Não é possivel tranferir para sua própria conta <<<\n\n")
            var_selecao: str = input("Deseja tentar novamente?\n"
                                     "[1] Sim\n"
                                     "[Outra tecla] Não\n"
                                     "-> ")
            match var_selecao:
                case '1': 
                    continue
                case _:
                    informacoes_de_usuario(login_usuario)
        
        try:
            # Pedindo um valor de transferência
            valor_para_transferir: float = float(input(f"Informe o valor que deseja transferir para {usuario_para_transferir}: "))
        
        # caso o usuário não coloque um número
        except ValueError:
            print("Por favor, informe apenas números", end='')
            tres_pontinhos()
            continue

        # Verificando se o valor para transferir excede o saldo da conta
        if valor_para_transferir > lista_de_usuarios[login_usuario][1]:
            limpar_linhas(1)
            var_selecao: str = input("\nO valor de transferência excede seu saldo\n\n[1] Colocar outro valor\n[outra tecla] Voltar para o menu\n---> ")
            if var_selecao == '1':
                continue
            else: 
                informacoes_de_usuario(login_usuario)
        
        # Pedindo senha para finalizar o deposito
        senha_usuario: str = input("SENHA: ")

        verificacao_de_senha(senha_usuario, login_usuario)

        lista_de_usuarios[login_usuario][1] -= valor_para_transferir # Subtraindo o valor informado
        lista_de_usuarios[usuario_para_transferir][1] += valor_para_transferir # Adicionando o valor informado
        print(f"Transferência de R${valor_para_transferir:.2f} realizada com sucesso para {usuario_para_transferir}", end='')

        # Adicionando um texto para ver o extrato depois
        lista_de_usuarios[login_usuario][3].append(f"Transferência para {usuario_para_transferir}: R${valor_para_transferir:.2f}")
        lista_de_usuarios[usuario_para_transferir][3].append(f"Transferência de {login_usuario}: R${valor_para_transferir:.2f}")

        print("\nVoltando para o menu", end='')
        tres_pontinhos()
        break

    informacoes_de_usuario(login_usuario)


# Função para ver os movimentos da conta
def extrato_bancario(login_usuario: str) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f">>> EXTRATO BANCÁRIO DE {login_usuario.upper()} <<<\n")
    saldo_atual = lista_de_usuarios[login_usuario][1]
    print(f"Saldo atual: R${saldo_atual:.2f}\n")
    
    print("Histórico de Transações:")
    if not lista_de_usuarios[login_usuario][3]:
        print("Nenhuma transação realizada.")
    else:
        for transacao in lista_de_usuarios[login_usuario][3]:
            print(transacao)

    input("\nPressione Enter para voltar ao menu...")
    informacoes_de_usuario(login_usuario)


# Função que verifica se a senha está correta
def verificacao_de_senha(senha_usuario, login_usuario) -> None:
    
    # Verificando se a senha está correta
    tentativas = 3 

    # Verificando se a senha está errada
    while senha_usuario != lista_de_usuarios[login_usuario][0]:
        tentativas -= 1 
        # Caso as tentativas esgotem a conta será bloqueada
        if tentativas == 0:
            lista_de_usuarios[login_usuario][2] = 'locked'
            print("Sua conta foi bloqueada, por favor dirija-se a boca do caixa para realizar o desbloqueio: ")
            print("Retornando", end="")
            tres_pontinhos()
            main()
        senha_usuario = input(f"Senha inválida, tentativas restantes {tentativas}: ")
        

# função da animação dos pontinhos
def tres_pontinhos():
    for i in "...":
        print(i, end='')
        time.sleep(1)
    
if __name__ == "__main__":
    lista_de_usuarios: UserDatabase = {
        'joao_victor': ['100101', 1450.0, 'unlocked', []],
        'jose_gal': ['123456', 1800.0, 'unlocked', []],
        'leonardo_otolindo': ['654321', 2000.0, 'unlocked', []],
        'rolysson_prog': ['675432', 15000.0, 'unlocked', []]
    }

    main()