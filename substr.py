def substr(str, sub):
    i = 0
    while i < len(str):
        j = 0
        while j < len(sub):
            if str[i+j] == sub[j]:
                if j == len(sub)-1:
                    return i
                else:
                    j = j + 1
                    if i+j >= len(str):
                        return -1
            else:
                break
        i = i + 1
    return -1

