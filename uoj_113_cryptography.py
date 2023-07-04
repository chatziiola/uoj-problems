# We are asked to find the nth root of p
# from math import 

while True:
    try:
        n = int(input())
        p = int(input())
    except EOFError:
        break

    print(f"{round(p**(1/n))}")
