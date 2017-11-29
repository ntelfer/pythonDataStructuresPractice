class Node:
    def __init__(self, val="", lNode=None, rNode=None):
        self.value = val
        self.leftNode = lNode
        self.rightNode = rNode

    def insert(self, val):
        if val > self.value:
            if self.rightNode is None:
                self.rightNode = Node(val)
            else:
                self.rightNode.insert(val)
        else:
            if self.leftNode is None:
                self.leftNode = Node(val)
            else:
                self.leftNode.insert(val)

    def print(self):
        if self.leftNode is not None:
            self.leftNode.print()

        print(self.value)

        if self.rightNode is not None:
            self.rightNode.print()
