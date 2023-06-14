def calcular_soma(intervalo):
    soma = sum(intervalo)
    return soma

def main():
    intervalo = list(range(1, 101))  # Intervalo de 1 a 100 (inclusive)

    soma = calcular_soma(intervalo)

    print("Intervalo:", intervalo)
    print("Soma:", soma)

if __name__ == "__main__":
    main()
