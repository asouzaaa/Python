def calcular_soma_quadrados(valor1, valor2, valor3):
    soma_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2
    return soma_quadrados

def main():
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
    valor3 = int(input("Digite o terceiro valor inteiro: "))

    soma_quadrados = calcular_soma_quadrados(valor1, valor2, valor3)

    print("A soma dos quadrados dos valores é:", soma_quadrados)

if __name__ == "__main__":
    main()
