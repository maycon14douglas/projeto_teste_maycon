def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


def menu():
    print("\n=== CALCULADORA SIMPLES ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")


while True:
    menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                print("Resultado:", somar(num1, num2))
            elif opcao == "2":
                print("Resultado:", subtrair(num1, num2))
            elif opcao == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcao == "4":
                print("Resultado:", dividir(num1, num2))

        except ValueError:
            print("Erro: entrada inválida. Use apenas números.")
    else:
        print("Opção inválida. Tente novamente.")
