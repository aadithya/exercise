def subset_sum(subsets):
    output = []
    for subset in subsets:
        if not reduce(lambda x,y: x + y, subset):
            output.append(subset)

    return output

def subset(arr):
    if not len(arr):
        return [""]
    sub = subset(arr[1:])
    return [arr[0] + el for el in sub] + sub

if __name__ == "__main__":
    in_str = raw_input("Enter the array: ").split(',')
    print subset(in_str)

