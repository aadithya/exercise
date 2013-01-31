def three_sum(arr, k, n):
    if k == 0 and n == 0:
        return [[]]

    if not len(arr) or k <= 0 or n <= 0:
        return []

    if n == 1 and k == arr[0]:
        return [[arr[0]]]

    t_sum = three_sum(arr[1:],k - arr[0], n-1)
    return [t +[arr[0]] for t in t_sum] + three_sum(arr[1:], k , n)

if __name__ == "__main__":
    arr = [ int(word) for word in raw_input("Enter the array: ").split(",")]
    k = int(raw_input("Input the number: "))
    print three_sum(arr,k,3)
