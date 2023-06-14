def calcular_quadrado_soma(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    quadrado_soma = soma ** 2
    return quadrado_soma

def main():
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
    valor3 = int(input("Digite o terceiro valor inteiro: "))

    quadrado_soma = calcular_quadrado_soma(valor1, valor2, valor3)

    print("O quadrado da soma dos valores é:", quadrado_soma)

if __name__ == "__main__":
    main()
