
# The output displays the smallest positive angle in degrees between
# the hands for each time. The answer should between 0 degrees and 180
# degrees for all input times. Display each angle on a line by itself
# in the same order as the input. The output should be rounded to the
# nearest 1/1000, i.e., three places after the decimal point should be
# printed.


while True:
    try:
        hours, minutes = [int(i) for i in input().split(":")]
    except EOFError:
        break

    if hours == 0 and minutes == 0:
        break

    # 30 degrees each hour, and each hour is up to 12:
    # 6 degrees each minute
    if hours == 12:
        hourAngle = 0
    else:
        hourAngle = hours*30

    hourAngle += 30*(minutes/60)
    minAngle = 6*minutes

    # Χωρίς βλάβη της γενικότητας, έστω H μπροστά:
    # - Αν hourAngle - minAngle < 180: η γωνία δίνεται από hourAngle - minAngle
    # - Αλλιώς >= 180: 360-hourAngle + minAngle
    b = max(hourAngle, minAngle)
    c = min(hourAngle, minAngle)

    if b-c < 180:
        answer = b-c
    else:
        answer = 360 - b + c

    print(f"{answer:.3f}")
