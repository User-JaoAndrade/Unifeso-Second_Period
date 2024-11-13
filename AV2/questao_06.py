import time

if __name__ == "__main__":
    while True:
        num: int = int(input("Informe um número ímpar de 3 até 15: "))

        if (num % 2) == 0 or num == 1:
            print("\nInforme um número ÍMPAR maior que 1 e menor que 16")
            time.sleep(3)
            continue
        else: 
            break

