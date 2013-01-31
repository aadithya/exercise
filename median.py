def find_median(arr1, arr2):
    print arr1
    print arr2
    if len(arr1) == 2 and len(arr2) == 2:
        return False
    m1 =  len(arr1)/2  if len(arr1) % 2 else len(arr1)/2 - 1
    m2 =  len(arr2)/2  if len(arr2) % 2 else len(arr2)/2 - 1
    if arr1[m1] == arr2[m2]:
        return arr1[m1]
    elif arr1[m1] > arr2[m2]:
        return find_median(arr1[:m1+1], arr2[m2+1:])
    else:
        return find_median(arr1[m1+1:], arr2[:m2+1])

counter = 0
def find_in(a,b,n, start, end):
    global counter
    counter += 1
    if start > end:
        return False
    mid = start + (end - start)/2
    offset = n - mid - 1
    if offset < 0:
        if offset == -1 and b[0] >= a[mid]:
            return a[mid]
        else:
            return find_in(a,b,n, start, mid - 1)
    if offset >= len(b):
        return find_in(a,b,n, mid+1, end)

    if a[mid] == b[offset]:
        return a[mid]
    if a[mid] > b[offset]:
        if offset + 1 >= len(b) or a[mid] <= b[offset + 1]:
            return a[mid]
        else:
            return find_in(a,b,n, start, mid-1)
    else:
        return find_in(a, b, n, mid+1, end)


def find_binary_median(a,b):
    n = (len(a) + len(b))/2
    m = find_in(a,b, n, 0, len(a)-1)
    if not m:
        return find_in(b, a, n, 0 , len(b)-1)
    else:
        return m

if __name__ == "__main__":
    arr1 = [int(i) for i in raw_input("Enter the array: ").split(",")]
    arr2 = [int(i) for i in raw_input("Enter the array: ").split(",")]
    print find_binary_median(arr1, arr2)
    print counter

