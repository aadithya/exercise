def max_sum(arr):
    if len(arr) > 2:
        return max(arr[0] + max_sum(arr[2:]), arr[1] + max_sum(arr[3:]))
    else:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return max(arr[0], arr[1])

if __name__ == "__main__":
    arr = [ int(word) for word in raw_input("Enter the array: ").split(",")]
    print max_sum(arr)

