""" 2022-05-24
ACMICPC: 1052번 물병
<https://www.acmicpc.net/problem/1052>

:author: 1@1c1.dev
:param timestamp: 2022-05-24T12:57:00+0900
:comment: 토너먼트 관리하는 게임 같네요.
"""


def main(n: int, k: int):
    powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
              32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]
    recent = n

    for i in reversed(powers):
        if (i < n):
            n -= i
            k -= 1
            recent = i
            if (n <= k):
                return 0
            if (k == 0):
                break
    return recent - n


# 두개의 숫자를 입력 받아 알고리즘을 실행함
n, k = map(int, input().split())
print(main(n, k))


"""
def old(n: int, m: int):
    new_bottles = 0
    bottles = [1] * n

    while len(bottles) > m:
        # print(bottles)
        done = False
        i = 0
        while i < len(bottles) - 1:
            if (bottles[i] == bottles[i+1]):
                bottles[i] = bottles[i] + bottles[i+1]
                bottles.pop(i+1)
                done = True
            i += 1

        if (not done):
            new_bottles += 1
            bottles.append(1)

    return new_bottles
"""
