def converter_dolar_para_real(valor_dolar, cotacao_dolar):
    valor_real = valor_dolar * cotacao_dolar
    return valor_real

def main():
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    valor_dolar = float(input("Digite a quantidade de dólares disponível: "))

    valor_real = converter_dolar_para_real(valor_dolar, cotacao_dolar)

    print("O valor convertido para real é: R$", valor_real)

if __name__ == "__main__":
    main()
