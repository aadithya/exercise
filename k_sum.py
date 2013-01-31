def k_sum(arr, k):
    if not len(arr):
        return []
    if k == arr[0]:
        return [[k]] + k_sum(arr[1:],k)
    ret = k_sum(arr[1:], k)
    if k > arr[0]:
        k_n = k_sum(arr[1:], (k-arr[0]))
        for a in k_n:
            ret += [a + [arr[0]]]
    return ret

if __name__ == "__main__":
    num = raw_input("Enter the array:")
    arr =  [int(i) for i in num.split(",")]
    k = raw_input("Enter the sum:")
    print k_sum(arr, int(k))

