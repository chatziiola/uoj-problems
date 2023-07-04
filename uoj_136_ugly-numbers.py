# Ugly numbers are numbers whose only prime factors are 2,3 or 5.

# Since we will have to deal with large numbers this also has to be
# memory efficient


answer = [1]*1500
twop = 0
threep = 0
fivep = 0

# Even though this "works" it surely is not ideal:
# many numbers will get inserted again and again
for index in range(1,1500):
    tmp = min(2*answer[twop],
              3*answer[threep],
              5*answer[fivep])

    # Can't be lower than the previous one, just checking for 
    if tmp == answer[index-1]:
        # Fix indices
        # TODO, check again for validity
        if tmp == 2*answer[twop]:
            twop += 1
        if tmp == 3*answer[threep]:
            threep += 1
        if tmp == 5*answer[fivep]:
            fivep += 1

    tmp = min(2*answer[twop],
              3*answer[threep],
              5*answer[fivep])
    if tmp == 2*answer[twop]:
        twop += 1
    elif tmp == 3*answer[threep]:
        threep += 1
    else:
        fivep += 1
    answer[index] = tmp

# for number in answer:
#     print(number)

print(f"The 1500'th ugly number is {answer[1499]}.")
