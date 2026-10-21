
from collections import deque

def valid(m, c):
    mr, cr = 3 - m, 3 - c

    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (mr == 0 or mr >= cr))

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            return path

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            nm, nc, nb = new_state

            if valid(nm, nc) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

path = solve()

if path:
    print("Solution path (M, C, Boat):")
    for state in path:
        print(state)
else:
    print("No solution found")
