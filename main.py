# @author ibryans
# Uma simples engine de xadrez

# T: Torre
# C: Cavalo
# B: Bispo
# D: Dama
# R: Rei
# p: Peão


A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7

# Criando o tabuleiro usando uma matriz
board = [

    # ['T','P','_','_','_','_','P','T'],
    # ['C','P','_','_','_','_','P','C'],
    # ['B','P','_','_','_','_','P','B'],
    # ['T','P','_','_','_','_','P','T'],

    ['T','C','B','D','R','B','C','T'],
    ['P','P','P','P','P','P','P','P'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['P','P','P','P','P','P','P','P'],
    ['T','C','B','D','R','B','C','T'],
]

def get_position(x, y):
    # print('Casa ' + row + column+1)
    return board[x][y-1]



def get_possible_destination(piece_coord_X, piece_coord_Y):
    piece = board[piece_coord_X][piece_coord_Y]

    print(piece)
    print()

    if (piece == 'P'):

        # Mover 2 casas pra frente
        if (piece_coord_Y == 1):
            if (board[piece_coord_X][piece_coord_Y+2] == '_'):
                board[piece_coord_X][piece_coord_Y+2] == 'O'

        # Mover pra frente
        if (board[piece_coord_X][piece_coord_Y+1] == '_'):
            board[piece_coord_X][piece_coord_Y+1] == 'O'

        # Comer na diagonal direita
        if ((piece_coord_X < 7 and piece_coord_Y < 7)):
            if (board[piece_coord_X+1][piece_coord_Y+1] != '_'):
                board[piece_coord_X+1][piece_coord_Y+1] ='('.join([
                    board[piece_coord_X+1][piece_coord_Y+1],
                    ')'
                ])

        # Comer na diagonal esquerda
        if ((piece_coord_X > 0 and piece_coord_Y < 7)):
            if (board[piece_coord_X-1][piece_coord_Y+1] != '_'):
                board[piece_coord_X-1][piece_coord_Y+1] ='('.join([
                    board[piece_coord_X-1][piece_coord_Y+1],
                    ')'
                ])

    if (piece == 'T'):
        # percorrendo a linha
        for square in range (0, 7, 1):
            if (board[square][piece_coord_Y-1] == '_'):
                board[square][piece_coord_Y-1] = 'O'
        
        # percorrendo a coluna
        for square in range (0, 7, 1):
            if (board[piece_coord_X][square] == '_'):
                board[piece_coord_X][square] = 'O'

    show_board()


def show_board():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))

get_possible_destination(G,0)