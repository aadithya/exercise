def see_and_tell(seed, itr):
    for i in range(itr):
        j = 0
        p = ''
        out = ""
        while j < len(seed):
            count = 1
            p = seed[j]
            j += 1
            if j == len(seed):
                out = out + str(count) + seed[j - 1]
                break
            while seed[j] == p:
                count = count + 1
                j = j + 1
                if j == len(seed):
                    break
            out = out + str(count) + p
        seed = out
    return seed

if __name__ == "__main__":
    seed = raw_input("Seed: ")
    i = int(raw_input("Iter: "))
    print see_and_tell(seed, i)

