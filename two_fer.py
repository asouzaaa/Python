def two_fer(name):
    if name:
        return f"Um para {name}, um para mim!"
    else:
        return "Um para você, um para mim!"

def main():
    name = input("Digite um nome: ")
    result = two_fer(name)
    print(result)

if __name__ == "__main__":
    main()
