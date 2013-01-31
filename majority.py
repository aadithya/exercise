def majority(arr):
    count, element = 0, arr[0]
    for el in arr:
        if el == element:
            count += 1
        else:
            count = count - 1

        if count < 0:
            element = el
            count = 1

    return element

if __name__ == "__main__":
    in_arr = [int(i) for i in raw_input("Enter the array: ").split(",")]
    maj =  majority(in_arr)
    if reduce(lambda x,y: x + 1 if y == maj else x, in_arr, 0) > len(in_arr)/2:
        print maj
    else:
        print "No majority"


