import math


class FibheapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.p = 0
        self.child = 0
        self.left = 0
        self.right = 0
        self.mark = False

    def MakeChild(self, cn):
        cn.p = self
        self.degree = self.degree + 1
        if self.child == 0:
            self.child = cn
            cn.left = cn
            cn.right = cn
        else:
            c = self.child
            cn.right = c
            cn.left = c.left
            cn.left.right = cn

    def search_child(self, key):
        w = self
        v = self
        while True:
            if w.key == key:
                return w
            if w.child != 0:
                res = w.child.search_child(key)
            if res != 0:
                return res
            w = w.right
            if w == v:
                return 0

    def printNode(self):
        if self.child != 0:
            c = self.child
            cl = c.left
            while 1:
                print("%d has child %d" % (self.key, c.key))
                c.printNode()
                if cl == c:
                    break
                c = c.right


class FibHeap:
    def __init__(self, n, minx):
        self.n = n
        self.min = minx

    def insert(self, x):
        if self.min == 0:
            self.min = x
            x.left = x
            x.right = x
        else:
            x.right = self.min
            x.left = self.min.left
            x.left.right = x
            self.min.left = x
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def find_min(self):
        return self.min

    def Link(self, y, x):
        y.right.left = y.left
        y.left.right = y.right
        y.p = x
        x.degree = x.degree + 1
        y.mark = False
        if x.child == 0:
            x.child = y
            y.left = y
            y.right = y
        else:
            c = x.child
            y.right = c
            y.left = c.left
            y.left.right = y
            c.left = y

    def delete_min(self):
        i = self.min
        if i != 0:
            if i.child != 0:
                j = i.child
                while j.p != 0:
                    a = j.left
                    j.p = 0
                    j.left = 0
                    j.right = 0
                    j.right = self.min
                    j.left = self.min.left
                    j.left.right = j
                    self.min.left = j
                    j = a
            i.right.left = i.left
            i.left.right = i.right
            if i == i.right:
                self.min = 0
            else:
                self.min = i.right
                self.Consolidate()
            self.n -= 1
        return i

    def Consolidate(self):
        A = []
        for i in range(0, int(math.log(self.n, 2) + 1)):
            A.append(0)
        w = self.min
        t = w.left
        while 1:
            temp = w.right
            x = w
            d = x.degree
            while A[d] != 0:
                # print(A[d])
                y = A[d]
                if x.key > y.key:
                    v = x
                    x = y
                    y = v
                self.Link(y, x)
                A[d] = 0
                d = d + 1
            A[d] = x
            if w == t:
                break
            w = temp

        self.min = 0
        for i in range(0, int(math.log(self.n, 2) + 1)):
            if A[i] != 0:
                if self.min == 0:
                    self.min = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    A[i].right = self.min
                    A[i].left = self.min.left
                    A[i].left.right = A[i]
                    self.min.left = A[i]
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def find_node(self, key):
        w = self.min
        res = 0
        if w.key > key:
            return 0
        else:
            cr = w
            while 1:
                if cr.key == key:
                    return cr
                else:
                    if cr.child != 0:
                        res = cr.child.search_child(key)
                    if res != 0:
                        return res
                    cr = cr.right
                    if cr == w:
                        return 0

    def PrintHeap(self):
        root = self.min
        c = root
        print("min node is %d" % c.key)
        c.printNode()
        c = c.right
        while c != root:
            print("root number is %d" % c.key)
            c.printNode()
            c = c.right

