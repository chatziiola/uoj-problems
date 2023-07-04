# Compute B^p mod M 

# After searching online about properties of mod:
# - (ab)%m = ((a%m)(b%m))%m
def mod(b, p, m):
    if p == 0:
        return 1
    # Is odd
    if p & 1:
        return ((b % m) * mod(b, p-1, m))%m
    else:
        tmp = mod(b, int(p/2), m)
        return (tmp**2) % m

while True:
    try:
        b = int(input())
        p = int(input())
        m = int(input())
    except EOFError:
        break

    # print(f"Input: {b}, {p}, {m}")
    print(f"{mod(b,p,m)}")
    # Here is that we actually need try break
    try:
        input()
    except EOFError:
        break
