def calcular_salario_liquido(horas_trabalhadas, valor_hora_aula, percentual_desconto):
    salario_bruto = horas_trabalhadas * valor_hora_aula
    desconto = salario_bruto * (percentual_desconto / 100)
    salario_liquido = salario_bruto - desconto
    return salario_liquido

def main():
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    valor_hora_aula = float(input("Digite o valor da hora-aula: "))
    percentual_desconto = float(input("Digite o percentual de desconto do INSS: "))

    salario_liquido = calcular_salario_liquido(horas_trabalhadas, valor_hora_aula, percentual_desconto)

    print("Salário bruto:", horas_trabalhadas * valor_hora_aula)
    print("Salário líquido:", salario_liquido)

if __name__ == "__main__":
    main()

