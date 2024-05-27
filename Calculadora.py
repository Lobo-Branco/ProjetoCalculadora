def mostrar_menu():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def obter_entrada():
    operacao = input("Digite sua escolha (1/2/3/4): ")
    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return operacao, num1, num2
    else:
        print("Escolha inválida, tente novamente.")
        return obter_entrada()

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def calcular(operacao, num1, num2):
    if operacao == '1':
        resultado = adicionar(num1, num2)
    elif operacao == '2':
        resultado = subtrair(num1, num2)
    elif operacao == '3':
        resultado = multiplicar(num1, num2)
    elif operacao == '4':
        resultado = dividir(num1, num2)
    print(f"O resultado é: {resultado}")

def main():
    while True:
        mostrar_menu()
        operacao, num1, num2 = obter_entrada()
        calcular(operacao, num1, num2)
        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando...")
            break

if __name__ == "__main__":
    main()
