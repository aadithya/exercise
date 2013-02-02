def is_bst(arr, i):
    l = 2*i + 1
    r = 2*i + 2
    left , right = None, None
    if l < len(arr):
        left = arr[l]
    if r < len(arr):
        right = arr[r]
    if left or right:
        if left:
            if left < arr[i]:
                if right:
                    if right > arr[i]:
                        return is_bst(arr, l) and is_bst(arr, r)
                    else:
                        return False
                else:
                    return is_bst(arr,l)
            else:
                return False
        else:
            if right > arr[i]:
                return is_bst(arr,r)
            else:
                return False
    return True

def print_line(arr, q):
    out = []
    for i in q:
        if i >= len(arr):
            continue
        print arr[i],
        l = 2*i + 1
        r = 2*i + 2
        out.append(l)
        out.append(r)
    if len(out):
        print ""
        print_line(arr, out)

if __name__ == "__main__":
    in_arr = [int(i) for i in raw_input("Enter the array: ").split(",")]
    print_line(in_arr, [0])

