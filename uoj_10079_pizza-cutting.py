while True:
    n = 0
    try:
        n = int(input())
    except EOFError:
        break

    if n < 0:
        break

    print(1+int(n*(n+1)/2))
