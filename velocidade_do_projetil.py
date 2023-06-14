def calcular_velocidade(distancia, tempo):
    velocidade = (distancia * 1000) / (tempo * 60)
    return velocidade

def main():
    distancia = float(input("Digite a distância percorrida em quilômetros: "))
    tempo = float(input("Digite o tempo decorrido em minutos: "))

    velocidade = calcular_velocidade(distancia, tempo)

    print("A velocidade do projétil é:", velocidade, "metros por segundo")

if __name__ == "__main__":
    main()
