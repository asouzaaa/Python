def eh_palindromo(palavra):
    palavra_invertida = palavra[::-1]  # Inverte a palavra usando a técnica de slicing
    if palavra == palavra_invertida:
        return True
    else:
        return False

def main():
    entrada = input("Digite uma palavra, frase ou número: ")

    if eh_palindromo(entrada):
        print("Saída: True")
        print("Explicação: {} ao contrário é {}, logo é palíndromo".format(entrada, entrada))
    else:
        print("Saída: False")
        print("Explicação: {} ao contrário não é igual a {}, logo não é palíndromo".format(entrada, entrada[::-1]))

if __name__ == "__main__":
    main()

