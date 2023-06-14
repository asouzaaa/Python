def converter_real_para_dolar(valor_real, cotacao_dolar):
    valor_dolar = valor_real / cotacao_dolar
    return valor_dolar

def main():
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    valor_real = float(input("Digite a quantidade de reais disponível: "))

    valor_dolar = converter_real_para_dolar(valor_real, cotacao_dolar)

    print("O valor convertido para dólar é: US$", valor_dolar)

if __name__ == "__main__":
    main()
