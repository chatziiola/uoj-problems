# When I first read it I thought of the boundaries differently, and thought it was impossible :P

# f91(n)= f91(f91(n+11)), for n <= 100 
# otherwise it is n-10

n = int(input())

lessthanhundred = [0] * 101

def fninetyone(n):
    if n > 100:
        return n - 10
    else:
        if not lessthanhundred[n]:
            lessthanhundred[n] = fninetyone(fninetyone(n+11))
        return lessthanhundred[n]

while n != 0:

    if n > 100:
        print(f"f91({n}) = {n-10}")
    else:
        if not lessthanhundred[n]:
            fninetyone(n)
        print(f"f91({n}) = {lessthanhundred[n]}")
            
    n = int(input())



