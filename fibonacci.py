def fibonacci(numero):
    sequencia = [0, 1]  # Inicia a sequência com os dois primeiros números: 0 e 1

    while sequencia[-1] < numero:
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)

    return sequencia

def main():
    numero = int(input("Digite um número: "))

    # Chama a função fibonacci e armazena a sequência retornada
    resultado = fibonacci(numero)

    # Imprime a sequência de Fibonacci
    print("Sequência de Fibonacci:")
    for num in resultado:
        print(num)

if __name__ == "__main__":
    main()
