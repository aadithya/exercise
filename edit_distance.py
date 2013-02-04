def edit_distance(a,b):
    if not len(a):
        return len(b)
    if not len(b):
        return len(a)
    if a[0] == b[0]:
        return edit_distance(a[1:], b[1:])
    m1 = 0
    if len(a) < len(b):
        m1 = 1 + edit_distance(a, b[1:])
    m2 = 1 + edit_distance(a[1:], b[1:])
    m3 = 1 + edit_distance(a[1:], b)
    return min(m1,m2,m3) if m1 else min(m2,m3)


if __name__ == "__main__":
    str1 = raw_input("Enter the first string: ")
    str2 = raw_input("Enter the second string: ")
    print edit_distance(str1, str2)
