
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)
    return distance

def solve(start):
    queue = [(heuristic(start), 0, start, [])]
    visited = set()

    while queue:
        _, cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            return path

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        for dr, dc in [(1, 0), (-1, 0),
                       (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero]
                )
                new_state = tuple(new_state)

                if new_state not in visited:
                    h = heuristic(new_state)
                    heapq.heappush(
                        queue,
                        (cost + 1 + h, cost + 1,
                         new_state, path)
                    )

    return None

solution = solve(start)

if solution:
    print("Solution found:")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
