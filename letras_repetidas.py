def encontrar_primeira_letra_nao_repetida(texto):
    contador = {}

    # Contar a ocorrência de cada caractere no texto
    for char in texto:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1

    # Encontrar a primeira letra não repetida
    for char in texto:
        if contador[char] == 1:
            return char

    # Caso não exista letra não repetida
    return None

def main():
    texto = input("Digite o texto: ")

    primeira_letra = encontrar_primeira_letra_nao_repetida(texto)

    if primeira_letra:
        print(f"A primeira letra não repetida é: {primeira_letra}")
    else:
        print("Não existem letras que não se repetem no texto informado.")

if __name__ == "__main__":
    main()
