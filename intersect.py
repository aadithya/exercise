def intersect_all(arr):
    return reduce(intersection, arr)

def intersection(a, b):
    return [el for el in a if el in b]

if __name__ == "__main__":
    in_str = raw_input("Enter the array: ").split(',')
    print intersect_all(in_str)

