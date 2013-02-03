def lcs(str1, str2):
    t = [[0 for j in str2] for i in str1]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                t[i][j] = 1 + t[i-1][j-1] if i and j else 1
            else:
                if not i and not j:
                    t[i][j] = 0
                elif not i:
                    t[i][j] = t[i][j-1]
                elif not j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[len(str1)-1][len(str2)-1]

def lc_substring(s1, s2):
    t = [[0]* (len(s2) + 1) for i in range(len(s1) + 1)]
    max_val = 0
    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1 , -1):
            if s1[i] == s2[j]:
                t[i][j] = (t[i+1][j+1] + 1)

            max_val = max(max_val, t[i][j])
    return max_val

if __name__ == "__main__":
    str1 = raw_input("Enter the first string: ")
    str2 = raw_input("Enter the second string: ")
    print lc_substring(str1, str2)
