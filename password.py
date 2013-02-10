def password(s, j):
    a_map = {'a':['4','@','A'], 'i':['!','I'], 's':['S', '5']}
    out = []
    if j >= len(s):
        return [s]
    if s[j] in a_map:
        for w in a_map[s[j]]:
            out += password(s[:j] + w + s[j+1:], j + 1)
    if not len(out):
        return password(s, j+1)
    return out

if __name__ == "__main__":
    print password(raw_input("Enter: "), 0)
