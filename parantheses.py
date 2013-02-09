def par(n):
    if n == 1:
        return ["()"]
    else:
         return set(["()" + p for p in par(n-1)] + ["(" + p + ")" for p in par(n-1)] +
                 [p + "()" for p in par(n-1)] )

if __name__ == "__main__":
    n = int(raw_input("Enter the number of parantheses"))
    print par(n)
