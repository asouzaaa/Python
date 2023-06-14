def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def main():
    notas = []

    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)

    if media <= 5:
        print("Aprovado")
    else:
        print("Reprovado")

    print("Média obtida:", media)

if __name__ == "__main__":
    main()
