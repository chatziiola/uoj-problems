# n cigarettes:
# - smokes one by one
# - k > 1 butts, he can roll a new cigarette


while True:
    try:
        n, k = [int(i) for i in input().split()]
    except EOFError:
        break

    answer = 0
    butts = 0
    # Complexity O(log_k(n)), acceptable
    while n:
        answer += n
        butts += n
        n = butts // k
        butts %= k

    print(answer)
