def ordenar_decrescente(array):
    array.sort(reverse=True)

def main():
    array = []

    for i in range(12):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        array.append(elemento)

    ordenar_decrescente(array)

    print("Elementos ordenados em ordem decrescente:")
    for elemento in array:
        print(elemento)

if __name__ == "__main__":
    main()
