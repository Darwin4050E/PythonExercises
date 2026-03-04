def gamestate(board):
    """Determine the state of a tic-tac-toe game where x starts.

    :paaram board: list[str] - board of the game.
    :return: str - 1. win - if one and only one (X, O) has won the game.
                   2. draw - if no one has won the game.
                   3. ongoing - if no one has still won the game.

    :raises ValueError: 1. Wrong turn order: O started
                        2. Wrong turn order: X went twice
                        3. "Impossible board: game should have ended after the game was won"
    """
    n_o, n_x, n_spaces = 0, 0, 0
    for row in board:
        n_o += row.count("O")
        n_x += row.count("X")
        n_spaces += row.count(" ")
    if n_o > n_x: raise ValueError("Wrong turn order: O started")
    if n_x - 2 == n_o: raise ValueError("Wrong turn order: X went twice")
    is_O_win = False
    is_X_win = False
    diag_izq = "".join([board[index][index] for index in range(3)])
    diag_der = "".join([board[i_row][i_col] for i_row, i_col in zip(range(3), range(2, -1, -1))])
    for index in range(3):
        row = board[index]
        col = "".join([board[i_row][index] for i_row in range(3)])
        if "OOO" in [row, col, diag_izq, diag_der]: is_O_win = True
        if "XXX" in [row, col, diag_izq, diag_der]: is_X_win = True
    if is_X_win and is_O_win: raise ValueError("Impossible board: game should have ended after the game was won")
    if is_X_win or is_O_win: return "win"
    if not n_spaces: return "draw"
    return "ongoing"