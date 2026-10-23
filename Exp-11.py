def is_safe(region, color, assignment, graph):

    for neighbor in graph[region]:

        if assignment.get(neighbor) == color:

            return False

    return True

 

def solve_map_coloring(graph, colors, assignment=None):

    if assignment is None:

        assignment = {}

 

    if len(assignment) == len(graph):

        return assignment

 

    # Choose the next unassigned region

    region = next(r for r in graph if r not in assignment)

 

    for color in colors:

        if is_safe(region, color, assignment, graph):

            assignment[region] = color

            result = solve_map_coloring(graph, colors, assignment)

            if result:

                return result

            del assignment[region]

    return None

 

if __name__ == "__main__":

    graph = {

        "A": ["B", "C"],

        "B": ["A", "C", "D"],

        "C": ["A", "B", "D"],

        "D": ["B", "C"]

    }

    colors = ["Red", "Green", "Blue"]

    solution = solve_map_coloring(graph, colors)

    if solution:

        print("Map coloring solution:")

        for region, color in solution.items():

            print(f"{region}: {color}")

    else:

        print("No solution exists.")
