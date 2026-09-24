PIECES = "KQBRP"

# full piece name for --explain output
NAMES = {
    "P": "Pawn",
    "B": "Bishop",
    "R": "Rook",
    "Q": "Queen",
}

# move 4 direction [Bishop, Queen] and 4 direction (Rook, Queen)
# move row, move column
DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
STRAIGHTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# check board format
def parse_board(board):

    # case : board error , not string
    if not isinstance(board, str):
        return None

    # case : Sometimes there might be a \n at the end of the last line
    if board.endswith("\n"):
        board = board[:-1]
    rows = board.split("\n")
    size = len(rows)

    # case : empty board
    if size == 0 or rows[0] == "":
        return None

    # case : board error , not square
    for row in rows:
        if len(row) != size:
            return None

    # case : You must have 1 King piece
    king_count = 0
    for row in rows:
        king_count += row.count("K")
    if king_count != 1:
        return None
    return rows


# find king position all move row and column
def find_king(rows):
    for r in range(len(rows)):
        for c in range(len(rows)):
            if rows[r][c] == "K":
                return r, c
    return None


# find every piece that checks the king (piece, row, column, path)
def find_attackers(rows):
    size = len(rows)
    king_r, king_c = find_king(rows)
    attackers = []

    # Pawn
    for dc in (-1, 1):
        r = king_r + 1
        c = king_c + dc

        # case : out of board
        if 0 <= r < size and 0 <= c < size and rows[r][c] == "P":
            attackers.append(("P", r, c, []))

    # Bishop / Rook / Queen
    for directions, threats in ((DIAGONALS, "BQ"), (STRAIGHTS, "RQ")):
        for dr, dc in directions:
            r = king_r + dr
            c = king_c + dc
            path = []

            # case : out of board
            while 0 <= r < size and 0 <= c < size:
                square = rows[r][c]
                if square in PIECES:
                    if square in threats:
                        attackers.append((square, r, c, path))

                    # case : another piece blocks the way
                    break
                path.append((r, c))
                r += dr
                c += dc
    return attackers


# check if king is in check
def is_in_check(board):

    # case : board error
    rows = parse_board(board)
    if rows is None:
        return None
    return len(find_attackers(rows)) > 0


def checkmate(board):
    result = is_in_check(board)

    if result is None:
        print("Error")
    elif result:
        print("Success")
    else:
        print("Fail")


# show board with attack path (*) and which piece checks the king
def explain(board):

    rows = parse_board(board)

    # case : board error
    if rows is None:
        print("Error")
        return
    attackers = find_attackers(rows)

    grid = [list(row) for row in rows]

    # draw * on attack path
    for piece, r, c, path in attackers:
        for pr, pc in path:
            grid[pr][pc] = "*"
    for line in grid:
        print(" ".join(line))

    # case : no piece checks the king
    if not attackers:
        print("Fail: the King is safe")
        return

    print("Success: the King is in check by")
    for piece, r, c, path in attackers:
        print("  - %s at row %d, col %d" % (NAMES[piece], r + 1, c + 1))
