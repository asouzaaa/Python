def calcular_percentual(valor, total):
    percentual = (valor / total) * 100
    return percentual

def main():
    votos_validos_A = int(input("Digite a quantidade de votos válidos para o candidato A: "))
    votos_validos_B = int(input("Digite a quantidade de votos válidos para o candidato B: "))
    votos_validos_C = int(input("Digite a quantidade de votos válidos para o candidato C: "))
    votos_nulos = int(input("Digite a quantidade de votos nulos: "))
    votos_em_branco = int(input("Digite a quantidade de votos em branco: "))

    total_eleitores = votos_validos_A + votos_validos_B + votos_validos_C + votos_nulos + votos_em_branco

    percent_validos = calcular_percentual(votos_validos_A + votos_validos_B + votos_validos_C, total_eleitores)
    percent_validos_A = calcular_percentual(votos_validos_A, total_eleitores)
    percent_validos_B = calcular_percentual(votos_validos_B, total_eleitores)
    percent_validos_C = calcular_percentual(votos_validos_C, total_eleitores)
    percent_nulos = calcular_percentual(votos_nulos, total_eleitores)
    percent_em_branco = calcular_percentual(votos_em_branco, total_eleitores)

    print("Resultado da apuração:")
    print("Total de eleitores:", total_eleitores)
    print("Percentual de votos válidos em relação à quantidade de eleitores:", percent_validos, "%")
    print("Percentual de votos válidos do candidato A em relação à quantidade de eleitores:", percent_validos_A, "%")
    print("Percentual de votos válidos do candidato B em relação à quantidade de eleitores:", percent_validos_B, "%")
    print("Percentual de votos válidos do candidato C em relação à quantidade de eleitores:", percent_validos_C, "%")
    print("Percentual de votos nulos em relação à quantidade de eleitores:", percent_nulos, "%")
    print("Percentual de votos em branco em relação à quantidade de eleitores:", percent_em_branco, "%")

if __name__ == "__main__":
    main()
