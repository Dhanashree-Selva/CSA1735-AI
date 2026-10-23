def display(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()
 
def winner(board, mark):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == mark for i in line) for line in lines)
 
def main():
    board = [str(i) for i in range(1, 10)]
    player = "X"
    for _ in range(9):
        display(board)
        try:
            pos = int(input(f"Player {player}, choose position (1-9): ")) - 1
        except ValueError:
            print("Enter a number.")
            continue
        if not 0 <= pos < 9 or board[pos] in ("X", "O"):
            print("Invalid or occupied position.")
            continue
        board[pos] = player
        if winner(board, player):
            display(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    display(board)
    print("It's a draw!")
 
if __name__ == "__main__":
    main()
