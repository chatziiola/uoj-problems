cases = int(input()) + 1

for cs in range(1,cases):
    try:
        m,n = [int(i) for i in input().split()]
    except EOFError:
        break

    # Normally the answer would be mxn. The only problem would be if
    # there are identical concatenated words. The thing is that since
    # a word can be described as: word = m_i+n_i, and since, no m_i
    # might be equal to the other, no two words can be the same.
    # That's a lie, and i finally found my mistake:

    ### Set1: {ab, a} Set2: {c, bc}
    #### abc my occur from two different combinations, and I no longer
    #### believe there is a valid way to change other than set
    #### addition.
    

    # I have the feeling though, that the hidden edgecase(even though
    # problematically not mentioned in the definition) is when m_i =
    # n_i, in which case the concatenation does not take place. Nah
    # this must not be it.
    
    firstLanguage = set()
    for l in range(m):
        line = input()
        if line.isspace():
            continue
        firstLanguage.add(line)

    secondLanguage = set()
    thirdLanguage = set()

    # O(n*m)
    for l in range(n):
        try:
            line = input()
        except EOFError:
            break
        if line.isspace():
            continue
        secondLanguage.add(line)
        # Hash table O(1)
        for word in firstLanguage:
            thirdLanguage.add(word+line)

    # print(f"First language: {firstLanguage}")
    # print(f"Second language: {secondLanguage}")

    print(f"Case {cs}: {len(thirdLanguage)}")
