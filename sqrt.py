def sqrt(num, left, right):
    mid = left + (right - left)/2
    midsq = mid * mid
    error = num - midsq
    if (error > 0 and error < 0.001) or (error < 0 and error > -0.001):
        return mid
    elif error < 0:
        return sqrt(num, left, mid)
    else:
        return sqrt(num, mid, right)


if __name__ == "__main__":
    num = float(raw_input("Enter the number:"))
    print sqrt(num, 0 , num/2)

