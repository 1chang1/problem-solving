""" 2022-06-25
ACMICPC: 1041번 주사위
<https://www.acmicpc.net/problem/1041>

:author: 1@1c1.dev
:param timestamp: 2022-06-25T15:23:00+0900
:comment: 좀 생각해봐야하는 문제네요! 면이 맞닿을 수 있는지 체크하는 과정이 필요합니다.
"""


def main(n: int, values: list):
    if (n == 1):
        return sum(values) - max(values)

    impossible = [(0, 5), (1, 4), (2, 3)]
    p1 = min(values)
    p2 = 100
    p3 = 150

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if ((i, j) not in impossible):
                p2 = min(p2, values[i] + values[j])
                for k in range(j+1, len(values)):
                    if ((i, k) not in impossible and (j, k) not in impossible):
                        p3 = min(p3, values[i] + values[j] + values[k])

    result = p1 * ((n-1) * (n-2) * 4 + pow(n-2, 2))
    result += p2 * (2*n-3) * 4
    result += p3 * 4

    return result


n = int(input())
values = list(map(int, input().split()))
print(main(n, values))

# n = 1
# 0p * 0, 1p * 0, ~, 5p * 1 => 1

# n = 2
# 0p * 0, 1p * 0, 2p * 4, 3p * 4 => 8

# n = 3
# 0p * 2, 1p * 9, 2p * 12, 3p * 4 => 27

# n = 4
# 0p * 12((n-2)^2 * (n-1)), 1p * 28((n-2)*(n-1)*4 + (n-2)^2), 2p * 20((2n-3) * 4), 3p * 4(0 or 4) => 64

# A B C D E F
# 1 2 3 4 5 6
#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+
