def max(arr):
    max = float('-inf')
    max2 = float('-inf')
    for i in arr:
        if i > max2:
            if i > max:
                max2 = max
                max = i
            else:
                max2 = i
    return max, max2

class Node():
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def fast_max(arr):
    nodes = []
    for i in arr:
        nodes.append(Node(None, None, i))

    while len(nodes) > 1:
        nodes = create_tree(nodes)

    print nodes[0].value
    print find_second_max(nodes[0])

def create_tree(nodes):
    ret_val = []
    i = 0
    while i < len(nodes):
        if i+1 < len(nodes):
            ret_val.append(create_nodes(nodes[i], nodes[i+1]))
            i = i + 2
        else:
            ret_val.append(Node(None, nodes[i], nodes[i].value))
            i = i + 1
    return ret_val

def create_nodes(a,b):
    return Node(b, a, a.value) if a.value > b.value else Node(a, b, b.value)

def find_second_max(root):
    second = float('-inf')
    while(root and (root.left or root.right)):
        if root.left:
            if second < root.left.value:
                second = root.left.value
            root = root.right
        else:
            return second
    return second

def min_max(arr):
    i = 0
    min = float('inf')
    max = float('-inf')
    while i < len(arr):
        if i+1 >= len(arr):
            high, low = arr[i], arr[i]
            i = i + 1
        else:
            high, low = (arr[i], arr[i+1]) if arr[i] > arr[i + 1] else\
                (arr[i + 1], arr[i])
            i = i + 2
        if max < high:
            max = high
        if min > low:
            min = low
    print  max, min

