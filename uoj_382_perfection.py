from math import sqrt, ceil

# Proper divisor definition:
# a = bc,  bc are proper divisors iff b != c +- 1

# Number categorization:
# X = sum of perfect divisors
# Any number N can belong to one of the following categories:
# Perfect iff N = X
# Deficient iff X < N
# Abundant iff X > N


# Algorithm:
# For every integer, find X and perform the comparison:
# Lets analyze a little bit for proper divisors:
# N = a(a+1) = a^2 + a, and because a > 0:
# a^2 < N -> a < sqrt(N)


print("PERFECTION OUTPUT")
while True:
    try:
        Ns = [int(i) for i in input().split()]
    except EOFError:
        break

    while len(Ns) > 0:
        N = Ns.pop(0)

        if N == 0:
            print("END OF OUTPUT")
            exit()

        divisors = set([1])

        for i in range(2, ceil(sqrt(N)) +1):
            if N%i == 0 and not i*(i+1) == N:
                divisors.add(i)
                divisors.add(int(N/i))
                i  += 1

        divisors.discard(N)
        X = sum(divisors)

        # print(f"{divisors}, sum: {X}")
        if X == N:
            print(f"{N:>5}  PERFECT")
        elif X < N:
            print(f"{N:>5}  DEFICIENT")
        else:
            print(f"{N:>5}  ABUNDANT")
