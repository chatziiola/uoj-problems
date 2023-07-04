cases = int(input())


while cases:
    try:
        line = [int(i) for i in input().split()]
    except EOFError:
        break

    students = line[0]
    line.pop(0)

    # Main Algorithm:

    # Ideas
    # Sum (O(n)), Sort(O(nlogn)), Bisect(logn), Divide O(1)
    # Sum (O(n)), Compare while iterating O(n), Print(O(1))

    # The second one seems much better
    # So the final algorithm runs in O(n), seems pretty good.

    average = sum(line)/students
    aboveav = 0

    for student in line:
        if student > average:
            aboveav += 1

    print(f"{round((aboveav*100)/students,3):.3f}%")
            
    



