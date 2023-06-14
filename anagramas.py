def verificar_anagrama(string1, string2):
    # Remover espaços em branco e converter para letras minúsculas
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Verificar se as strings têm o mesmo comprimento
    if len(string1) != len(string2):
        return False

    # Criar dicionários para contar a ocorrência de cada caractere em cada string
    contagem1 = {}
    contagem2 = {}

    # Contar a ocorrência de cada caractere na primeira string
    for char in string1:
        if char in contagem1:
            contagem1[char] += 1
        else:
            contagem1[char] = 1

    # Contar a ocorrência de cada caractere na segunda string
    for char in string2:
        if char in contagem2:
            contagem2[char] += 1
        else:
            contagem2[char] = 1

    # Verificar se os dicionários de contagem são iguais
    if contagem1 == contagem2:
        return True
    else:
        return False

def main():
    # Solicitar as duas strings ao usuário
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    # Verificar se as strings são anagramas
    if verificar_anagrama(string1, string2):
        print("As strings são anagramas.")
    else:
        print("As strings não são anagramas.")

if __name__ == "__main__":
    main()
