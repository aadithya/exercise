class Node():
    def __init__(self, value):
        self.next = None
        self.value = value

def insert(head, value):
    if not head:
        return Node(value)
    ret_val = head
    node = Node(value)
    while head.next:
        head = head.next
    head.next = node
    return ret_val

def reverse(head):
    tmp1 = head
    tmp2 = None

    while head:
        head = head.next
        tmp1.next = tmp2
        tmp2 = tmp1
        tmp1 = head

    return tmp2

def print_list(head):
    if not head:
        print ""
    while head:
        print head.value,
        head = head.next

if __name__ == "__main__":
    in_str = raw_input("Enter the values in the linked list")
    head = None
    for i in in_str.split(","):
        head = insert(head, i)

    print_list(head)
    print ""
    print_list(reverse(head))

