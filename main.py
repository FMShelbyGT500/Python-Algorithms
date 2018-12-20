from Dijkstra import Dijkstra
import numpy as np


def enter_matrix():
    N = int(input("Enter nodes number:\n"))
    mat_enter = np.array([np.zeros(N) for i in range(N)])

    for i in range(N):
        for j in range(i+1, N):
            mat_enter[i][j] = mat_enter[j][i] = input(f'{i+1} > {j+1}: ')

    return mat_enter


matrix = np.array([
    [0,  7,  9,  0,  0, 14],
    [7,  0,  10, 15, 0, 0],
    [9,  10, 0,  11, 0, 2],
    [0,  15, 11, 0,  6, 0],
    [0,  0,  0,  6,  0, 9],
    [14, 0,  2,  0,  9, 0]
])

start_node = 0
end_node = 4


def main():
    path_search = Dijkstra(matrix, start_node, end_node)
    distances = path_search.distances
    path = path_search.path

    print()
    print(f"from {start_node} to {end_node} path is", distances[end_node])
    print()
    print(" > ".join(map(str, path)))


if __name__ == "__main__":
    main()
