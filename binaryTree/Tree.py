from binaryTree import Node


class BinaryTree:
    def __init__(self, node=None):
        self.node = node

    def insert(self, value):
        if self.node is None:
            self.node = Node.Node(value)
        else:
            self.node.insert(value)

    def print(self):
        if self.node is None:
            print("Tree is empty.")
        else:
            self.node.print()

    def find(self, value):
        currentNode = self.node

        while True:
            if currentNode is None:
                return None

            if currentNode.value == value:
                return currentNode
            elif currentNode.value < value:
                currentNode = currentNode.rightNode
            else:
                currentNode = currentNode.leftNode

    # Find the Lowest Common Ancestor given two nodes
    # Assumes that the nodes do exist in the tree
    # O(log(n) + k) where n is number of nodes and k is depth of LCA node
    def LCA(self, val1, val2):
        visited = []
        position = self.node
        while True:
            visited.append(position)
            if position.value > val1:
                position = position.leftNode
            elif position.value < val1:
                position = position.rightNode
            else:
                break

        last, position = self.node, self.node
        for node in visited:
            if node.value != position.value:
                break
            elif position.value > val2:
                position = position.leftNode
                last = node
            else:
                position = position.rightNode
                last = node

        return last
