def insert(arr, i):
    arr.append(i)
    p = len(arr) - 1
    par = p/2
    while True:
        if arr[par] <= arr[p]:
            return
        arr[par], arr[p] = arr[p], arr[par]
        if not par:
            return
        else:
            p, par = par, par/2

def heapify(arr, i):
    if i >= len(arr):
        return
    l, r = 2*i + 1, 2*i + 2
    smallest = i
    if l < len(arr) and arr[l] < arr[i]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest)

def build_heap(arr):
    n = len(arr)
    for i in range(n/2, -1, -1):
        heapify(arr,i)

if __name__ == "__main__":
    in_arr = []
    [insert(in_arr, i) for i in raw_input("Enter the array: ").split(",")]
    #build_heap(in_arr)
    print in_arr

