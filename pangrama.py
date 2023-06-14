import string

def eh_pangrama(frase):
    # Remove espaços em branco e converte todas as letras para minúsculas
    frase = frase.replace(" ", "").lower()

    # Cria um conjunto vazio para armazenar as letras encontradas na frase
    letras_encontradas = set()

    # Percorre cada caractere na frase
    for caractere in frase:
        # Verifica se o caractere é uma letra do alfabeto
        if caractere.isalpha():
            letras_encontradas.add(caractere)

    # Verifica se todas as letras do alfabeto foram encontradas na frase
    alfabeto = set(string.ascii_lowercase)
    return letras_encontradas == alfabeto

def main():
    frase = input("Digite uma frase: ")

    if eh_pangrama(frase):
        print("A frase é um pangrama.")
    else:
        print("A frase não é um pangrama.")

if __name__ == "__main__":
    main()
