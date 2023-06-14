def trocar_valores(a, b):
    a, b = b, a
    return a, b

def main():
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    a, b = trocar_valores(a, b)

    print("Valores trocados:")
    print("A =", a)
    print("B =", b)

if __name__ == "__main__":
    main()
