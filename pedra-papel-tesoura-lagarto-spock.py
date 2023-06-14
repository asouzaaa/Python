def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"

    regras = {
        "Tesoura": ["Papel", "Lagarto"],
        "Papel": ["Pedra", "Spock"],
        "Pedra": ["Lagarto", "Tesoura"],
        "Lagarto": ["Spock", "Papel"],
        "Spock": ["Tesoura", "Pedra"]
    }

    if jogador2 in regras[jogador1]:
        return "Jogador 1 venceu!"
    elif jogador1 in regras[jogador2]:
        return "Jogador 2 venceu!"
    else:
        return "Entrada inválida. Tente novamente."

def main():
    jogador1 = input("Jogador 1, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ")
    jogador2 = input("Jogador 2, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ")

    resultado = jokenpo(jogador1, jogador2)
    print(resultado)

if __name__ == "__main__":
    main()



