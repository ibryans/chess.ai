# @author B. S. Oliveira
# Uma simples engine de xadrez

# Criando o tabuleiro usando uma matriz
board = [
    ['T','P','-','-','-','-','P','T'],
    ['C','P','-','-','-','-','P','C'],
    ['B','P','-','-','-','-','P','B'],
    ['D','P','B','-','-','-','P','D'],
    ['R','P','-','P','-','-','P','R'],
    ['B','P','C','-','-','-','P','B'],
    ['C','P','-','-','-','-','P','C'],
    ['T','P','-','-','-','-','P','T'],
]

# Retorna a casa da peça selecionada
def get_square_position(coord_X, coord_Y):
    position_dict = {
        "0": "A",
        "1": "B",
        "2": "C",
        "3": "D",
        "4": "E",
        "5": "F",
        "6": "G",
        "7": "H",
    }
    x = position_dict[str(coord_X)]
    y = coord_Y+1
    return (str(x) + str(y))

# Retorna o nome da peça selecionada
def get_piece_name(piece):
    match piece:
        case 'T': return 'Torre'
        case 'C': return 'Cavalo'
        case 'B': return 'Bispo'
        case 'D': return 'Dama'
        case 'R': return 'Rei'
        case 'P': return 'Peão'



# Mostra os possíveis caminhos para a peça clicada
# Parâmetros:
#   coord_X: A - H
#   coord_Y: 0 - 7
def get_possible_destination(coord_X, coord_Y):
    
    # Se tiver selecionado uma casa vazia, não tem ação
    if (board[coord_X][coord_Y] == '-'):
        return

    piece = board[coord_X][coord_Y]
    print('Peça selecionada: '
        + str(get_piece_name(piece))
        + ' '
        + str(get_square_position(coord_X, coord_Y))
        + '\n')
        

    if (piece == 'P'):

        # Mover 1 casa pra frente
        if (board[coord_X][coord_Y+1] == '-'):
            board[coord_X][coord_Y+1] = '.'

        # Mover 2 casas pra frente
        if (coord_Y == 1):
            if (board[coord_X][coord_Y+1] == '.' and board[coord_X][coord_Y+2] == '-'):
                board[coord_X][coord_Y+2] = '.'

        # Comer na diagonal direita
        if ((coord_X < 7 and coord_Y < 7)):
            if (board[coord_X+1][coord_Y+1] != '-'):
                board[coord_X+1][coord_Y+1] = 'X'

        # Comer na diagonal esquerda
        if ((coord_X > 0 and coord_Y < 7)):
            if (board[coord_X-1][coord_Y+1] != '-'):
                board[coord_X-1][coord_Y+1] = 'X'        

    if (piece == 'T'):
        # percorrendo a linha
        for square in range (0, 7, 1):
            if (board[square][coord_Y-1] == '-'):
                board[square][coord_Y-1] = '.'
        
        # percorrendo a coluna
        for square in range (0, 7, 1):
            if (board[coord_X][square] == '-'):
                board[coord_X][square] = '.'

    show_board()


def show_board():
    for y in range(7, -1, -1):
        for x in range(0, 8, 1):
            print(str(board[x][y]), end=' ')
        print()

get_possible_destination(1,1)