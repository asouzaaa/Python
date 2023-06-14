def converter_romano_para_inteiro(s):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in s:
        valor = valores[c]
        if valor > prev:
            total += valor - 2 * prev
        else:
            total += valor
        prev = valor
    return total

def main():
    numeral_romano = input("Digite o numeral romano: ")
    numero_inteiro = converter_romano_para_inteiro(numeral_romano)
    print(f"Entrada: s = \"{numeral_romano}\"")
    print(f"Saída: {numero_inteiro}")
    print(f"Explicação: {numeral_romano} = {numero_inteiro}.")

if __name__ == "__main__":
    main()
