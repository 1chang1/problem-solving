""" 2022-05-25
ACMICPC: 2178번 물병
<https://www.acmicpc.net/problem/2178>

:author: 1@1c1.dev
:param timestamp: 2022-05-25T23:32:00+0900
:comment: 쉬운 BFS 문제네요.
"""


def main(n: int, m: int, matrix):
    visited: list(tuple) = []
    queue: list(tuple) = [(0, 0, 1)]

    while queue:
        (i, j, d) = queue.pop(0)

        if ((i, j) == (n - 1, m - 1)):
            return d

        if ((i, j) not in visited):
            visited.append((i, j))

            if (i + 1 < n and matrix[i + 1][j] == 1):
                queue.append((i + 1, j, d + 1))
            if (i - 1 >= 0 and matrix[i - 1][j] == 1):
                queue.append((i - 1, j, d + 1))
            if (j + 1 < m and matrix[i][j + 1] == 1):
                queue.append((i, j + 1, d + 1))
            if (j - 1 >= 0 and matrix[i][j - 1] == 1):
                queue.append((i, j - 1, d + 1))
    return -1


n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))

print(main(n, m, matrix))
