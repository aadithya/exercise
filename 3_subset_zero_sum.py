def subset(in_arr, num):
    if num <= 0:
        return [[]]

    if not len(in_arr):
        return []

    sub_arr = in_arr[1:]

    sub = subset(sub_arr, num - 1)
    sub = [s + [in_arr[0]] for s in sub]
    return sub + subset(sub_arr, num)

def zero_sum(in_arr):
    for arr in in_arr:
        if not reduce(lambda x,y: x+y, arr):
            print arr

if __name__ == "__main__":
    in_arr = [int(i) for i in raw_input("Enter the array: ").split(",")]
    zero_sum(subset(in_arr, 3))

