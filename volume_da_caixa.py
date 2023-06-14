def calcular_volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

def main():
    comprimento = float(input("Digite o valor do comprimento da caixa: "))
    largura = float(input("Digite o valor da largura da caixa: "))
    altura = float(input("Digite o valor da altura da caixa: "))

    volume = calcular_volume(comprimento, largura, altura)

    print("O volume da caixa retangular é:", volume)

if __name__ == "__main__":
    main()
