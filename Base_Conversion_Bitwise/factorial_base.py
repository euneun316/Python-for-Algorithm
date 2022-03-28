import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


while True:
    n = sys.stdin.readline().strip()
    # 마지막 줄에 0
    if int(n) == 0:
        break

    n_len = len(n)
    result = 0

    for i in range(n_len):
        # 7 * 3! + 1 * 2! + 9 * 1!
        result += int(n[i]) * factorial(n_len - i)
    print(result)