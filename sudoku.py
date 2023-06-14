def validar_sudoku(tabuleiro):
    def verificar_linhas():
        for linha in tabuleiro:
            if len(set(linha)) != 9 or any(valor < 1 or valor > 9 for valor in linha):
                return False
        return True

    def verificar_colunas():
        for coluna in range(9):
            valores_coluna = [tabuleiro[linha][coluna] for linha in range(9)]
            if len(set(valores_coluna)) != 9 or any(valor < 1 or valor > 9 for valor in valores_coluna):
                return False
        return True

    def verificar_regioes():
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                regiao = [
                    tabuleiro[row][col]
                    for row in range(i, i + 3)
                    for col in range(j, j + 3)
                ]
                if len(set(regiao)) != 9 or any(valor < 1 or valor > 9 for valor in regiao):
                    return False
        return True

    if verificar_linhas() and verificar_colunas() and verificar_regioes():
        return True
    else:
        return False


def encontrar_celulas_incorretas(tabuleiro):
    celulas_incorretas = []

    for i in range(9):
        for j in range(9):
            valor = tabuleiro[i][j]
            if valor < 1 or valor > 9 or tabuleiro[i].count(valor) > 1 or any(tabuleiro[row][j] == valor for row in range(9) if row != i):
                celulas_incorretas.append((i, j))

    return celulas_incorretas


def main():
    # Exemplo de tabuleiro de Sudoku preenchido parcialmente
    tabuleiro = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if validar_sudoku(tabuleiro):
        print("O tabuleiro de Sudoku é válido.")
    else:
        print("O tabuleiro de Sudoku contém erros.")

        celulas_incorretas = encontrar_celulas_incorretas(tabuleiro)
        if celulas_incorretas:
            print("Células incorretas:")
            for celula in celulas_incorretas:
                print(f"Célula ({celula[0]},{celula[1]})")
        else:
            print("Não há células incorretas.")

main()

