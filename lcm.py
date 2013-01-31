def lcm_many(arr):
    return reduce(lcm, arr)

def lcm(a,b):
    return a * b/gcd(a,b)

def gcd(a,b):
    if b:
        return gcd(b, a%b)
    else:
        return a

if __name__ == "__main__":
    input_el = [int(i) for i in raw_input("Enter the integers").split(',')]
    print lcm_many(input_el)

