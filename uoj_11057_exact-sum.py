from bisect import bisect_left

case = 0

while True:
    try:
        n = int(input())
        books = [int(i) for i in input().split()]
        m = int(input())
    except EOFError:
        break

    # O(nlgn)
    books.sort()

    priceDifference = m
    solution = []

    # print(f"{books}")
    # O(nlgn)
    for firstIndex in range(n):
        if books[firstIndex]> m/2:
            break
        pairIndex = bisect_left(books, m-books[firstIndex], lo=firstIndex+1)
        if pairIndex != n and books[firstIndex]+ books[pairIndex] == m and abs(books[firstIndex]- books[pairIndex]) < priceDifference:
            priceDifference = abs(books[firstIndex]-books[pairIndex])
            solution = [books[firstIndex], books[pairIndex]]
    
    # Output
    print(f"Peter should buy books whose prices are {solution[0]} and {solution[1]}.\n")

    # Blank Line at the end of each case (input)
    try:
        input()
    except EOFError:
        break
