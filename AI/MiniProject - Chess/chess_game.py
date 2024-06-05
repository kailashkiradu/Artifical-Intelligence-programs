import chess
import chess.svg


def display_board(board):
    return chess.svg.board(board=board)


def player_move():
    move_uci = input("Enter your move (in UCI format, e.g., 'e2e4'): ")
    return chess.Move.from_uci(move_uci)


def ai_move(board, depth=2):
    best_move = None
    best_eval = float('-inf')

    for move in board.legal_moves:
        board.push(move)
        eval = -minimax(board, depth - 1, False)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval


def evaluate_board(board):
    # Simple evaluation function (counts material)
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            evaluation += piece_value(piece)
    return evaluation


def piece_value(piece):
    if piece.piece_type == chess.PAWN:
        return 1
    elif piece.piece_type == chess.KNIGHT:
        return 3
    elif piece.piece_type == chess.BISHOP:
        return 3
    elif piece.piece_type == chess.ROOK:
        return 5
    elif piece.piece_type == chess.QUEEN:
        return 9
    elif piece.piece_type == chess.KING:
        return 1000
    return 0


def main():
    board = chess.Board()

    while not board.is_game_over():
        print(display_board(board))

        # Player move
        move = player_move()
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Invalid move. Try again.")
            continue

        # AI move
        if not board.is_game_over():
            ai_move_result = ai_move(board)
            board.push(ai_move_result)

    print(display_board(board))
    print("Game over. Result: {}".format(board.result()))


if __name__ == "__main__":
    main()
