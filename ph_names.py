def get_letters(num):
    offset = num*3
    return "abcdefghijklmnopqrstuvwxyz"[offset:offset+3]

def names(number):
    if not len(number):
        return [""]
    ret_val = []
    possib = names(number[1:])
    for l in get_letters(int(number[0])):
        ret_val = ret_val + [ l + p for p in possib]
    return ret_val

if __name__ == "__main__":
    str1 = raw_input("Enter the phone number: ")
    print names(str1)

