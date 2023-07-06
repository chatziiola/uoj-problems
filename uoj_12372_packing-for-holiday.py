# maybe the easiest one I've seen so far

cases = int(input()) + 1

for case in range(1,cases):
    try:
        l,w,h = [int(i) for i in input().split()]
    except EOFError:
        break

    if l <= 20 and w <= 20 and h <=20:
        answer = "good"
    else:
        answer = "bad"

    print(f"Case {case}: {answer}")
