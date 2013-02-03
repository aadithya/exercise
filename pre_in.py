def construct(pre, in_o):
    if not len(pre):
        return None

    r = find(pre[0], in_o)
    l_in = in_o[:r]
    r_in = in_o[r+1:]
    if len(r_in):
        r_p = find(r_in[0], pre)
        r_pre = pre[r_p:]
        l_pre = pre[1:r_p]
    else:
        r_pre = []
        l_pre = pre[1:]

    return Node(pre[0], construct(l_pre, l_in), construct(r_pre, r_in))


def find(v, arr):
    for i, a in enumerate(arr):
        if a == v:
            return i
    return -1

class Node():
    def __init__(self, val, left, right ):
        self.val = val
        self.left = left
        self.right = right

def post(root):
    if not root:
        return
    post(root.left)
    post(root.right)
    print root.val,

if __name__ == "__main__":
    preorder = [int(i) for i in raw_input("Enter the preorder: ").split(",")]
    inorder = [int(i) for i in raw_input("Enter the inorder: ").split(",")]
    root = construct(preorder, inorder)
    post(root)

