
if __name__ == "__main__":
    n = 10 ** 5
    for a in range(1, n):
        a3 = a**3
        if a3 > n: break
        for b in range(a, n):
            b3 = b**3
            if a3 + b3 > n: break
            for c in range(a+1, n):
                c3 = c**3
                if c3 > a3 + b3: break
                for d in range(c, n):
                    d3 = d**3
                    if c3 + d3 > a3 + b3: break
                    if a3 + b3 == c3 + d3:
                        print a,b,c,d, a3 + b3

