import copy

def Min(current_state,alpha = float('-inf'), beta = float('inf')):

    if end(current_state):
        return evaluate(current_state), current_state
    current_best_value = float('inf')
    best_move = None

    for next_state in get_next_states(current_state):
        opponents_best_move_value,_ = Max(next_state)
        if opponents_best_move_value < current_best_value:
            current_best_value = opponents_best_move_value
            best_move = next_state
        if current_best_value <= alpha:
            return current_best_value, next_state
        if current_best_value < beta:
            beta = current_best_value

    return current_best_value, best_move
def Max(current_state):
    if end(current_state):
        return evaluate(current_state), current_state

    best_move = None
    current_best_value = float('-inf')

    for next_state in get_next_states(current_state):
        opponents_best_move_value,_ = Min(next_state)
        if opponents_best_move_value > current_best_value:
            best_move = next_state
            current_best_value = opponents_best_move_value

    if current_best_value >= beta:
        return current_best_value, next_state
    if current_best_value > alpha:
        alpha = current_best_value

    return current_best_value, best_move


class XOState:
    empty = ' '
    def __init__(self):
        self.board = [
            [XOState.empty, XOState.empty, XOState.empty],
            [XOState.empty, XOState.empty, XOState.empty],
            [XOState.empty, XOState.empty, XOState.empty]
        ]
        self.current_player = 'X'
        self.last_move = None
        self.move_count = 0

    def play_move(self, move):
        i,j = move[0], move[1]
        self.board[i][j] = self.current_player
        self.last_move = move
        self.move_count += 1
        self.current_player = 'X' if self.current_player == 'O' else 'O'
    
    def draw_board(self):
        print('|'.join(self.board[0]))
        print('|'.join(self.board[1]))
        print('|'.join(self.board[2]))
        print()

def get_winner(current_state: XOState):
    board = current_state.board

    # kolone
    for i in range(0,3):
        if board[0][i] != XOState.empty and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # redovi
    for i in range(0,3):
        if board[i][0] != XOState.empty and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # dijagonale
    if board[0][0] != XOState.empty and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != XOState.empty and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def end(current_state:XOState):
    winner = get_winner(current_state)
    return winner is not None or current_state.move_count == 9

def read_next_move_from_stdin():
    move = input().split(',')
    return [int(move[0]), int(move[1])]
    
def get_next_states(current_state:XOState):
    result = []
    for i in range(0,3):
        for j in range(0,3):
            if current_state.board[i][j] == XOState.empty:
                next_state = copy.deepcopy(current_state)
                next_state.play_move([i,j])
                result.append(next_state)
    return result

def evaluate(current_state:XOState):
    winner = get_winner(current_state)
    result = 0

    if winner == 'X':
        result = 1
    elif winner == 'O':
        result = -1
    return result


def get_next_computer_move(current_state:XOState,func):
    _,state = func(current_state)
    return state.last_move

if __name__ == '__main__':
    game = XOState()
    game.draw_board()

    while True:
        next_move = read_next_move_from_stdin()
        game.play_move(next_move)
        game.draw_board()

        if get_winner(game) == 'X':
            print("Player X won!\n")
            break
        if end(game):
            print("Tie!\n")
            break
        
        next_move = get_next_computer_move(game, Min)

        game.play_move(next_move)
        game.draw_board()
        if get_winner(game) == 'O':
            print("Player O won!\n")
            break