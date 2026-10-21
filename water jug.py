
from collections import deque

def water_jug():
    start = (0, 0)
    goal = 2

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == goal:
            return path

        amount = min(b, 4 - a)
        states = [
            (4, b), (a, 3), (0, b), (a, 0),
            (a + amount, b - amount),
            (a - min(a, 3 - b), b + min(a, 3 - b))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

result = water_jug()

if result:
    print("Steps (4L jug, 3L jug):")
    for state in result:
        print(state)
else:
    print("Solution not found")
