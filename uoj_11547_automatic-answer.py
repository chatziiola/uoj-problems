# After playing around with the given equation on paper, i managed to bring it down to the following form
# answer = (15 n + 62) // 10 % 10
# This expression was actually wrong 

cases = int(input())

while cases:
    try:
        n = int(input())
    except EOFError:
        break

    print(f"{ abs(315*n+36962)//10 %10}")

    cases -= 1
