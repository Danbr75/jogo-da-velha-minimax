# Cria o tabuleiro com 9 posições vazias
tabuleiro = [" " for _ in range(9)]

# Função para exibir o tabuleiro em formato 3x3
def exibir_tabuleiro():
    print()
    for i in range(0, 9, 3):
        print(f"{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Função que verifica se o jogador venceu
def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0,1,2], [3,4,5], [6,7,8],  # Linhas
        [0,3,6], [1,4,7], [2,5,8],  # Colunas
        [0,4,8], [2,4,6]            # Diagonais
    ]
    return any(all(tabuleiro[pos] == jogador for pos in combinacao) for combinacao in combinacoes_vencedoras)

# Verifica se deu empate (nenhum espaço vazio)
def verificar_empate(tabuleiro):
    return all(casa != " " for casa in tabuleiro)

# Função Minimax - o coração do jogo
def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, "X"):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, "O"):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Calcula a melhor jogada possível para o computador
def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    return melhor_posicao

# Função principal do jogo
def jogar_jogo():
    print("=== Bem-vindo ao Jogo da Velha com Minimax! ===")
    print("Você é o X. O computador é o O.")
    print("Posições do tabuleiro:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8\n")

    while True:
        exibir_tabuleiro()

        # Jogada do jogador humano (X)
        while True:
            try:
                jogada = int(input("Sua jogada (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except:
                print("Entrada inválida. Digite um número de 0 a 8.")

        tabuleiro[jogada] = "X"

        if verificar_vencedor(tabuleiro, "X"):
            exibir_tabuleiro()
            print("🎉 Você venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("😐 Empate!")
            break

        # Jogada do computador (O)
        print("🤖 Computador está pensando...")
        pos = melhor_jogada(tabuleiro)
        tabuleiro[pos] = "O"

        if verificar_vencedor(tabuleiro, "O"):
            exibir_tabuleiro()
            print("💻 O computador venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("😐 Empate!")
            break

# Execução do jogo
jogar_jogo()
