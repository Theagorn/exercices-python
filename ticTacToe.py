# Rules
# In random order

# a game is over when all fields in a row are taken by a player
# players take turns taking fields until the game is over
# a game is over when all fields in a diagonal are taken by a player
# a game is over when all fields are taken
# --------------- there are two players in the game (X and O)
# --------------- a game has nine fields in a 3x3 grid
# a game is over when all fields in a column are taken by a player
# a player can take a field if not already taken

#---------------------------------------------------------------------

import random


player_X = "X"
player_O = "O"
# grid = [[" "] * 3] * 3
grid = [[" " for i in range(3)] for j in range(3)]
first = random.choice([player_X, player_O])
winner = None

def afficher_grille():
    for i in grid:
        print(i)

def tour(player):
    saisie = int(input("Choisissez une case à remplir (1  -9): "))
    ligne = (saisie - 1) // 3
    colonne = (saisie - 1) % 3
    # print(ligne, colonne)
    if grid[ligne][colonne] == " ":
        grid[ligne][colonne] = player
        player = player_O if player == player_X else player_X
        return player
    else:
        print("Cette case est déjà prise, choisissez-en une autre")
        return player

def check_winner():
    # vérifier les lignes
    for ligne in grid:
        if ligne[0] == ligne[1] == ligne[2] != " ":
            return ligne[0]

    # vérifier les colonnes
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != " ":
            return grid[0][col]
    # vérifier les diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return grid[0][2]
    # vérifier si la grille est pleine
    for ligne in grid:
        for case in ligne:
            if case == " ":
                return None
    return "Égalité"

# afficher_grille()
while winner is None:
    print("---------------------------------------------\nAu tour du joueur", first)
    afficher_grille()
    first = tour(first)
    winner = check_winner()
    if winner == "Égalité":
        print("La partie se termine par une égalité")

    elif winner in [player_X, player_O]:
        print("Le vainqueur est le joueur", winner)
        afficher_grille()


