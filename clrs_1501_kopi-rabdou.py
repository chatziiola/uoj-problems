 # Πρόβλημα: Δοθέντος πίνακος τιμών για το εκτάστοτε μήκος, και μήκους
 # $n$, βρες το μέγιστο κέρδος που μπορεί να προκύψει από την διάσπαση
 # της ράβδου

n = int(input())

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
maxprofit = [0] * (n+1)

for length in range(1,1+n):
    if length < p.__len__():
        maxprofit[length] = p[length-1]
    for i in range(1,min(p.__len__(),length)):
        maxprofit[length] = max(maxprofit[length], maxprofit[length - i] + maxprofit[i])


# for length in range(0, 1+n):
    # print(f"For length {length}: profit {maxprofit[length]}")

print(maxprofit[n])
