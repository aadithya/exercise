def roman_to_int(roman):
    r_map = {'I':1,'V':5 , 'X': 10, 'L': 50, 'C':100, 'IV':4, 'VI':6, 'IX':9, 'XI':11,'XL': 40 , 'LX': 60, 'XC':90, 'CX': 110}
    output = 0
    for i in range(len(roman) - 1, -1 , -2):
        second = r_map[roman[i]]
        first = r_map[roman[i-1]] if i > 0  else None

        if first:
            if second <= first:
                output = output + first + second
            else:
                output = output + second - first
        else:
            output += second
    return output

def roman(roman):
    r_map = {'I':1,'V':5 , 'X': 10, 'L': 50, 'C':100, 'IV':4, 'VI':6, 'IX':9, 'XI':11,'XL': 40 , 'LX': 60, 'XC':90, 'CX': 110}
    total = state = last = 0
    for l in roman:
        if state:
            total += r_map[l]
            state = 0
        elif r_map[l] <= last:
            total += r_map[l]
        else:
            state = 1
            total+= l - 2*last

        last = r_map[l]

    return total

if __name__ == "__main__":
    r= raw_input("Enter the roman numeral:")
    print roman(r)
