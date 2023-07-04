while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 0:
        break

    while (n % 10 != n):
        # Sum digits
        tmpsum = 0
        while n != 0:
            tmpsum += n % 10
            n //= 10
        # Assign sum to n
        n = tmpsum

    print(f"{n}")
        
