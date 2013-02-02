
def reverse(arr):
    n = len(arr) - 1
    for i in range(len(arr)/2):
        arr[i], arr[n - i] = arr[n - i], arr[i]
    return arr

def palindrome(s):
    n = len(s) - 1
    for i in range(len(s)/2):
        if s[i] != s[n - i]:
            return False
    return True

if __name__ == "__main__":
    #in_arr = [int(i) for i in raw_input("Enter the array: ").split(",")]
    #print reverse(in_arr)
    string = raw_input("Enter the string: ")
    print palindrome(string)
