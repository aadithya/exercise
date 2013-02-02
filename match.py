def match(s1, s2, k):
    if k > len(s1) or k > len(s2):
        return False
    for i in range(len(s1)):
        if i + k >= len(s1):
            return False
        if s1[i:i+k] in s2:
            return True
    return False

if __name__ == "__main__":
    str1 = raw_input("First string: ")
    str2 = raw_input("Second string: ")
    k = int(raw_input("Number of characters: "))
    print match(str1, str2, k)
