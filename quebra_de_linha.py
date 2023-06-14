def quebrar_linhas(frase, colunas):
    palavras = frase.split()  # Separa a frase em uma lista de palavras
    linhas = []  # Lista para armazenar as linhas quebradas

    linha_atual = ""
    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= colunas:
            # Se a palavra couber na linha atual, adiciona-a à linha
            if linha_atual:
                linha_atual += " "
            linha_atual += palavra
        else:
            # Caso contrário, adiciona a linha atual à lista de linhas e começa uma nova linha com a palavra
            linhas.append(linha_atual)
            linha_atual = palavra

    # Adiciona a última linha à lista de linhas
    linhas.append(linha_atual)

    return linhas


def main():
    frase = input("Digite a frase: ")
    colunas = int(input("Digite a quantidade de colunas: "))

    linhas_quebradas = quebrar_linhas(frase, colunas)

    # Imprime as linhas quebradas
    for linha in linhas_quebradas:
        print(linha)


if __name__ == "__main__":
    main()
