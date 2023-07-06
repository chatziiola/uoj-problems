# Generate wave form, according to amplitude and frequency

cases = int(input())

notfirst = False

while True:
    try:
        input() # blank line
        a = int(input())
        f = int(input())
    except EOFError:
        break

    if notfirst:
        print()
    else:
        notfirst = True

    # Compute the string Instead of making a function for that and
    # losing significant time, with memory jumps etc.
    line = "1"
    for i in range(2,a+1):
        line += "\n" + str(i)*(i)
    for i in range(a-1, 0, -1):
        line += "\n" + str(i)*(i) 
    
    print(line)
    for i in range(f-1):
        print()
        print(line)
