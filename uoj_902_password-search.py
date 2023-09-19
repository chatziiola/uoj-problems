# Kinda memory intense this one. Also, this worsens the lookup time.
while True:
    try:
        length, message = input().split()
        length = int(length)
    except EOFError:
        break

    myMap = dict([])
    # O(n^2)?
    for i in range(length, len(message)+1):
        if message[i-length:i] in myMap:
            myMap[message[i-length:i]] += 1
        else:
            myMap[message[i-length:i]] = 1

    reps = 1
    # O(n)
    for key in myMap:
        if myMap[key] > reps:
            answ = key
            reps = myMap[key]
        
    print(answ)

            
