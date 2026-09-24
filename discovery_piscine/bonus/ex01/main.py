import sys
from checkmate import checkmate, explain


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def main():
    args = sys.argv[1:]
    show = False

    # case : if first argument is --explain then show explain mode
    if len(args) > 0 and args[0] == "--explain":
        show = True
        args = args[1:]
    
    # case : don't have any board file then print how to use :3
    if len(args) == 0:
        print("usage: python3 main.py [--explain] board.chess ...")
        return
    
    # case : read each board file and checkmate it
    for path in args:
        board = read_file(path)

        if board is None:
            print("Error")
        elif show:
            explain(board)
        else:
            checkmate(board)

if __name__ == "__main__":
    main()
