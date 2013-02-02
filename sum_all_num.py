
def find_all_nums(n):
    out = []
    if n == 0:
        return [[]]
    for i in range(1, n + 1):
        nums = find_all_nums(n-i)
        for v in nums:
            out.append(v + [i])
    return out

if __name__ == "__main__":
    print find_all_nums(int(raw_input("Enter the number: ")))
