def permute(arr):
    output= []
    if len(arr) == 1:
        return [arr]
    for i in range(len(arr)):
        if i > 0:
            perm_arr = permute(arr[:i] + arr[i+1:])
        else:
            perm_arr = permute(arr[i+1:])
        for perms in perm_arr:
            output.append([arr[i]] + perms)
    return output

def n_permute(arr, n):
    output = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        if i > 0:
            perm_arr = n_permute(arr[:i] + arr[i+1:], n-1)
        else:
            perm_arr = n_permute(arr[i+1:], n-1)

        for perms in perm_arr:
            output.append([arr[i]] + perms)

    return output

if __name__ == "__main__":
    in_str = raw_input("Enter the array: ")
    in_arr = [int(i) for i in in_str.split(',')]
    #print permute(in_arr)
    print n_permute(in_arr, 3)

