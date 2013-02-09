def find_path(m, n, a, b, x, y):
    if x > m or y > n:
        return -1
    if x == a and y ==b:
        return 0
    m1 = find_path(m, n, a, b, x+y, y)
    m2 = find_path(m, n, a, b, x, x+y)
    if m1 == -1:
        if m2 != -1:
            return m2 + 1
        else:
            return -1
    else:
        if m2 != -1:
            return min(m1, m2) + 1
        else:
            return m1 + 1

if __name__ == "__main__":
    (m, n, a, b) = [int(i) for i in raw_input("Enter:").split(",")]
    print find_path(m, n, a, b, 1, 1)
