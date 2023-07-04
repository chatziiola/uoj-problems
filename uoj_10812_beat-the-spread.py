cases = int(input())

while cases:
    try:
        s, d = [int(i) for i in input().split()]
    except EOFError:
        break

    if d > s or (s+d)/2 != (s+d)//2 :
        print("impossible")
    else:
        # print(f"{(s+d)/2} {(s-d)/2}")
        print(f"{int((s+d)/2)} {int((s-d)/2)}")

    # cases -= 1
