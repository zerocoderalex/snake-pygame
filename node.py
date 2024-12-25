class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def print_tree(node, level=0, label="."):
    if node is not None:
        print_tree(node.right, level + 1, "R")
        print(" " * (level * 4) + label + ": " + str(node.value))
        print_tree(node.left, level + 1, "L")

# Пример использования
if __name__ == "__main__":
    root = None
    keys = [5, 3, 8, 1, 4, 7, 9]
    for key in keys:
        root = insert(root, key)

    print("Построенное дерево:")
    print_tree(root)




