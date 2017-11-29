from binaryTree import Tree


tree = Tree.BinaryTree()

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for val in values:
    tree.insert(val)

print("In-order traversal: ")
tree.print()
print()

print("parent of 3,4:", tree.LCA(3, 4).value)
print("parent of 3,10:", tree.LCA(3, 10).value)
print("parent of 1,14:", tree.LCA(1, 14).value)
print("parent of 4,7:", tree.LCA(4, 7).value)
print("parent of 1,7:", tree.LCA(1, 7).value)

print()
print(tree.find(10).value)
print(tree.find(20))
