# We are told that no two people will ahve the same name nor birthdate

daPeople = []
people = int(input())

for person in range(people):
    name, day,month,year = input().split()
    if len(month) == 1:
        month = "0"+month
    if len(day) == 1:
        day = "0"+day
    daPeople.append((name,int(year+month+day)))

daPeople.sort(key=lambda x: x[1])

# for entry in mySet:
#     print(f"\t{entry}")

print(daPeople[-1][0])
print(daPeople[0][0])
