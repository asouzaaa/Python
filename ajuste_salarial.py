def calcular_novo_salario(salario, percentual):
    novo_salario = salario + (salario * percentual / 100)
    return novo_salario

def main():
    salario = float(input("Digite o salário mensal: "))
    percentual = float(input("Digite o percentual de reajuste: "))

    novo_salario = calcular_novo_salario(salario, percentual)

    print("Novo salário:", novo_salario)

if __name__ == "__main__":
    main()
