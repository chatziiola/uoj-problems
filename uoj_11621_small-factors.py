from bisect import bisect_left

mylist = []

for i in range(32):
    for j in range(32-i):
        mylist.append(2**i * 3**j)

mylist.sort()

while True:
    try:
        m = int(input())
        if m == 0:
            break
    except EOFError:
        break

    print(mylist[bisect_left(mylist, m)])
