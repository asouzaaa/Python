def calcular_troco(total_a_pagar, valor_pago):
    valor_troco = valor_pago - total_a_pagar

    cedulas = [100, 50, 10, 5, 1]
    moedas = [0.5, 0.10, 0.05, 0.01]

    troco_em_cedulas = []
    troco_em_moedas = []

    for cedula in cedulas:
        qtd_cedulas = int(valor_troco / cedula)
        if qtd_cedulas > 0:
            troco_em_cedulas.append((cedula, qtd_cedulas))
            valor_troco -= cedula * qtd_cedulas

    for moeda in moedas:
        qtd_moedas = int(valor_troco / moeda)
        if qtd_moedas > 0:
            troco_em_moedas.append((moeda, qtd_moedas))
            valor_troco -= moeda * qtd_moedas

    return troco_em_cedulas, troco_em_moedas

def main():
    total_a_pagar = float(input("Valor total a pagar: "))
    valor_pago = float(input("Valor efetivamente pago: "))

    troco_em_cedulas, troco_em_moedas = calcular_troco(total_a_pagar, valor_pago)

    if len(troco_em_cedulas) == 0 and len(troco_em_moedas) == 0:
        print("Não há troco a ser fornecido.")
    else:
        print("Troco em cédulas:")
        for cedula, quantidade in troco_em_cedulas:
            print(f"{quantidade} cédula(s) de R${cedula:.2f}")

        print("Troco em moedas:")
        for moeda, quantidade in troco_em_moedas:
            print(f"{quantidade} moeda(s) de R${moeda:.2f}")

if __name__ == "__main__":
    main()



