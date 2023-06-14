def calcular_soma_pares(inicio, fim):
    soma = 0
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
    return soma

def main():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    soma_pares = calcular_soma_pares(inicio, fim)

    print("A soma dos números pares no intervalo é:", soma_pares)

if __name__ == "__main__":
    main()
