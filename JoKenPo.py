def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif (
            (jogador1 == "Pedra" and jogador2 == "Tesoura") or
            (jogador1 == "Tesoura" and jogador2 == "Papel") or
            (jogador1 == "Papel" and jogador2 == "Pedra")
    ):
        return "Jogador 1 venceu!"
    else:
        return "Jogador 2 venceu!"

def main():
    jogador1 = input("Jogador 1, escolha entre Pedra, Papel ou Tesoura: ")
    jogador2 = input("Jogador 2, escolha entre Pedra, Papel ou Tesoura: ")

    resultado = jokenpo(jogador1, jogador2)
    print(resultado)

if __name__ == "__main__":
    main()
