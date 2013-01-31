class Node():
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

def insert(root, data):
    if not root:
        return Node(None, None, data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def least_common_ancestor(root, v1, v2):
    if not root:
        return None

    a = least_common_ancestor(root.left, v1, v2)
    if isinstance(a, Node):
        return a

    b = least_common_ancestor(root.right, v1, v2)
    if isinstance(b, Node):
        return b

    if a == v1 and b == v2:
        return root

    if b == v1 and a == v2:
        return root

    if  v1 == root.data and (a == v2 or b == v2):
        return root

    if  v2 == root.data and (a == v1 or b == v1):
        return root

    if a:
        return a

    if b:
        return b

    if root.data == v1:
        return v1

    if root.data == v2:
        return v2

def print_tree(root):
    if root:
        print_tree(root.left)
        print root.data
        print_tree(root.right)

def print_level(arr):
    child_arr = []
    for i in arr:
        if i:
            print i.data,
            child_arr.append(i.left)
            child_arr.append(i.right)
    print ""
    if len(child_arr):
        print_level(child_arr)

def find_nth_el(root, n, count = None):
    if not count:
        count = [0]
    if root:
        find_nth_el(root.left, n, count)
        count[0] = count[0] + 1
        if count[0] == n:
            print root.data
        find_nth_el(root.right, n, count)

def longest_path(root):
    if root:
        return max(longest_path(root.left), longest_path(root.right)) + 1
    return 0

if __name__ == "__main__":
    root = None
    for i in range(5):
        data = int(raw_input("insert the node value nr %d: " % i))
        root = insert(root, data)

    v1, v2 = tuple(int(i) for i in raw_input("Input the value to search for: ").split(","))
    print_level([root])
    print least_common_ancestor(root, v1, v2).data

