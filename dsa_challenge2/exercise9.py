class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_leaves(root, leaves=None):
    if leaves is None:
        leaves = []

    if root is None:
        return leaves
    if root.left is None and root.right is None:
        leaves.append(root.value)
        return leaves
    
    count_leaves(root.left, leaves)
    count_leaves(root.right, leaves)
        
    return leaves

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
print(count_leaves(root))