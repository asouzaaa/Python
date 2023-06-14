def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def main():
    numero = int(input("Digite um número: "))
    fatorial = calcular_fatorial(numero)
    print("O fatorial de {} é: {}".format(numero, fatorial))

if __name__ == "__main__":
    main()
