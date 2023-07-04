# There seems to be a pretty easy O(n) algorithm for this one:
# Simply mimic "mabu"'s behaviour. However there has to be a better option,
# Simply finding all the divisors is not good enough:

# the solution is O(1) and described below, good thinking

from math import sqrt

while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 0:
        break

    # For every i that divides n, n/i also divides it. Thus, it is
    # always a pair of numbers *are they integers though*? Yeah, due
    # to the divisibility clause in the problem's definition

    # except for the case where an integer l exists such as l^2 = n.
    # It is only under this circumastance that the starting condition
    # may change

    if sqrt(n).is_integer():
        print("yes")
    else:
        # print(f"{sqrt(n)}, no")
        print(f"no")
        

    
