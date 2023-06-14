import math

def calcular_area(raio):
    area = math.pi * raio ** 2
    return area

def main():
    raio = float(input("Digite o valor do raio: "))

    area = calcular_area(raio)

    print("A área da circunferência é:", area)

if __name__ == "__main__":
    main()
