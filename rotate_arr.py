def rotate_arr(arr, num):
    new_arr = [0 for i in arr]
    for i in range(len(arr)):
        new_pos = (i + num) % len(arr)
        new_arr[new_pos] = arr[i]
    return new_arr

if __name__ == "__main__":
    in_str = raw_input("Enter the array")
    in_arr = [int(i) for i in in_str.split(",")]
    print rotate_arr(in_arr, 3)

