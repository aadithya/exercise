def find_start(in_arr, start, end):
    if start >= end:
        return start
    if start == (end - 1):
        return start if in_arr[start] < in_arr[end]\
                else end
    mid = start + (end - start)/2
    if in_arr[mid] < in_arr[start]:
        return find_start(in_arr, start, mid)
    return find_start(in_arr, mid, end)

def binary_search(in_arr, start, end, val):
    if start >= end:
        return start if in_arr[start] == val \
                else -1
    mid = start + (end - start)/2
    print start,mid, end
    if val == in_arr[mid]:
        return mid
    if not mid:
        return binary_search(in_arr, mid + 1, end, val)

    if in_arr[start] <= in_arr[mid - 1]:
        if val <= in_arr[mid - 1] and val >= in_arr[start]:
            return binary_search(in_arr, start, mid - 1, val)
        else:
            return binary_search(in_arr, mid + 1, end, val)
    else:
        if val >= in_arr[mid + 1] and val <= in_arr[end]:
            return binary_search(in_arr, mid + 1, end, val)
        else:
            return binary_search(in_arr, start, mid - 1, val)

if __name__ == "__main__":
    in_arr = [int(i) for i in raw_input("Enter the sorted array").split(",")]
    print binary_search(in_arr, 0, len(in_arr) - 1, int(raw_input("Val to search: ")))
