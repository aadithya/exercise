
def subset(arr):
    if not len(arr):
        return [[]]
    sub = subset(arr[1:])
    return [[arr[0]] + s for s in sub] + sub

if __name__ == "__main__":
    in_arr = [int(i) for i in raw_input("Enter the array: ").split(",")]
    print subset(in_arr)
