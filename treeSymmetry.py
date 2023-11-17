class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is None) != (root2 is None) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

def build_tree():
    val = int(input("Enter the value for the root node: "))
    root = TreeNode(val)
    nodes = [root]

    while nodes:
        current = nodes.pop(0)

        left_val = int(input(f"Enter the left child value of {current.val}: "))
        if left_val != -1:
            current.left = TreeNode(left_val)
            nodes.append(current.left)

        right_val = int(input(f"Enter the right child value of {current.val}: "))
        if right_val != -1:
            current.right = TreeNode(right_val)
            nodes.append(current.right)

    return root

root = build_tree()

if is_symmetric(root):
    print("The tree is symmetric.")
else:
    print("The tree is not symmetric.")