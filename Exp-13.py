def minimax(tree, maximizing):
    if isinstance(tree, int):
        return tree
    values = [minimax(child, not maximizing) for child in tree]
    return max(values) if maximizing else min(values)
 
if __name__ == "__main__":
    # Leaves are utility values; levels alternate MAX and MIN.
    game_tree = [
        [3, 5, 2],
        [9, 1, 4],
        [6, 7, 8]
    ]
    scores = [minimax(branch, False) for branch in game_tree]
    best_move = max(range(len(scores)), key=lambda i: scores[i])
    print("Branch scores:", scores)
    print("Best move: Branch", best_move + 1)
    print("Best score:", scores[best_move])
