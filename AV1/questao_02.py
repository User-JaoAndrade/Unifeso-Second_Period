# Desenvolva um conversor de números romanos para decimais e vice-versa. O programa
# deve lidar com números de 1 a 3999. Implemente funções separadas para cada direção
# de conversão e inclua verificações de entrada válida

import os

# Função para limpar o terminal
def limpar_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para converter decimal para romano
def decimal_para_romano(numero: int) -> str:
    if numero < 1 or numero > 3999:
        raise ValueError("O número deve estar entre 1 e 3999.")
    
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

# Função para converter romano para decimal
def romano_para_decimal(romano: str) -> int:
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    valor_anterior = 0
    
    for simbolo in romano[::-1]:
        valor_atual = valores.get(simbolo)
        if valor_atual is None:
            raise ValueError(f"'{simbolo}' não é um símbolo romano válido.")
        
        if valor_atual < valor_anterior:
            total -= valor_atual
        else:
            total += valor_atual
        valor_anterior = valor_atual
    
    if total < 1 or total > 3999:
        raise ValueError("O número romano deve resultar em um valor entre 1 e 3999.")
    
    return total

# Menu para o usuário escolher a conversão
def menu() -> None:
    while True:
        limpar_terminal()  # Limpa o terminal antes de exibir o menu
        print("\n>>> CONVERSOR DE NÚMEROS ROMANOS <<<")
        print("[1] Converter decimal para romano")
        print("[2] Converter romano para decimal")
        print("[outra tecla] Sair")

        escolha = input("\nEscolha uma opção (1, 2 ou 3): ")

        if escolha == "1":
            try:
                numero_decimal = int(input("Digite um número decimal (1 a 3999): "))
                romano = decimal_para_romano(numero_decimal)
                print(f"O número {numero_decimal} em romano é: {romano}")
            except ValueError as e:
                print(e)
            except Exception:
                print("Entrada inválida. Digite um número válido.")
        
        elif escolha == "2":
            numero_romano = input("Digite um número romano: ").upper()
            try:
                decimal = romano_para_decimal(numero_romano)
                print(f"O número romano {numero_romano} em decimal é: {decimal}")
            except ValueError as e:
                print(e)
            except Exception:
                print("Entrada inválida. Digite um número romano válido.")
        
        else:
            print("Saindo do programa...")
            break
        

# Iniciar o programa
if __name__ == "__main__":
    menu()
