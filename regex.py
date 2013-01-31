def match(s1,s2):
    state = 0
    j = 0
    start = -1
    for i in range(len(s1)):
        if j >= len(s2):
            if state == 1 or state == 3:
                return start
            return -1
        if s2[j] == '*':
            j = j + 1
            if not state:
                start = i
            if j == len(s2) - 1:
                return start
            state = 2
        elif not state:
            if s1[i] == s2[j]:
                state = 1
                start = i
                j = j + 1
            else:
                j = 0
                continue
        elif state == 1:
            if s1[i] == s2[j]:
                j = j + 1
            else:
                j = 0
                state = 0
                continue
        elif state == 2:
            if s1[i] == s2[j]:
                j = j + 1
                state = 3
            else:
                j = j + 1

        elif state == 3:
            if s1[i] == s2[j]:
                j = j + 1
            else:
                state = 2
                j = j + 1

    return start

if __name__ == "__main__":
    s1 = raw_input("Enter the regex:")
    s2 = raw_input("Enter the string")
    print match(s2, s1)

