def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

def main():
    numeros = []
    continuar = True

    while continuar:
        numero = float(input("Digite um número: "))
        numeros.append(numero)

        opcao = input("Deseja inserir mais números? (S/N): ")
        if opcao.lower() != 's':
            continuar = False

    media = calcular_media(numeros)
    print("A média dos números informados é:", media)

if __name__ == "__main__":
    main()
