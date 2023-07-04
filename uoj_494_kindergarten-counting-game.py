import re

while True:
    try:
        line = input()
    except EOFError:
        break

    pattern = r'[^a-zA-z\s]|[\[\]`\\]'
    stringList = re.sub(pattern, ' ', line).split()
    # print(f"{stringList}")
    print(f"{len(stringList)}")
