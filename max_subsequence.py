def max_sub(in_arr):
    max_sum = float('-inf')
    sum_so_far = 0
    start = 0
    end = 0

    for i,el in enumerate(in_arr):
        sum_so_far += el
        end = i
        if sum_so_far > max_sum:
            max_sum = sum_so_far
            max_start = start
            max_end = end

        if sum_so_far < 0:
            sum_so_far = 0
            start = i + 1

    print max_start, max_end
    return max_sum


if __name__ == "__main__":
    in_str = raw_input("Input Arr: ")
    in_arr = [int(i) for i in in_str.split(",")]
    print max_sub(in_arr)
