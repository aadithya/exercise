def merge(a):
    min_heap = Heap()
    for i in range(len(a)):
        min_heap.insert(i, a[i].pop(0))

    out = []
    while(len(min_heap)):
        min_el = min_heap.extract_min()
        out.append(min_el.v)
        i = min_el.i
        if len(a[i]):
            min_heap.insert(i, a[i].pop(0))
    return out

class Node():
    def __init__(self,index, val):
        self.i = index
        self.v = val

class Heap():
    def __init__(self):
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        return str([a.v for a in self.arr])

    def insert(self, index, v):
        self.arr.append(Node(index, v))
        i = len(self.arr) - 1
        par  = len(self.arr) / 2 - 1
        arr = self.arr
        while par > -1:
            if arr[par].v > arr[i].v:
                arr[par], arr[i] = arr[i], arr[par]
            else:
                return
            i = par
            par  = (i + 1) / 2 - 1

    def heapify(self, i):
        a = self.arr
        l = 2*i + 1
        r = 2*i + 2
        if l < len(a):
            m = i
            if r < len(a):
                if a[i].v < a[l].v and a[i].v < a[r].v:
                    return
                if a[l].v < a[i].v:
                    m = l
                if a[r].v < a[i].v and a[r].v < a[l].v:
                    m = r
            else:
                if a[i].v < a[l].v:
                    return
                if a[l].v < a[i].v:
                    m = l
            a[m], a[i] = a[i], a[m]
            self.heapify(m)

    def extract_min(self):
        ret_val = self.arr[0]
        self.arr[0] = self.arr[len(self.arr) - 1]
        self.arr.pop()
        self.heapify(0)
        return ret_val

class Node():
    def __init__(self, i, v):
        self.i = i
        self.v = v


if __name__ == "__main__":
    in_arr = [[int(j) for j in i.split(",")] for i in raw_input("Enter the array: ").split(".")]
    print merge(in_arr)
