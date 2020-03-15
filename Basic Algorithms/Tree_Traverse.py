class TreeNode():
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None




def preOrder(root):
    if not root:
        return []
    left = preOrder(root.left)
    right = preOrder(root.right)
    # print(left)
    return [root.val] + left + right


def inOrder(root):
    if not root:
        return []
    left = preOrder(root.left)
    right = preOrder(root.right)

    return left +  [root.val] +  right

def postOrder(root):
    if not root:
        return []

    left = preOrder(root.left)
    right = preOrder(root.right)
    return left + right + [root.val]








if __name__ == "__main__":
    root  = TreeNode(1)
    root.left  = TreeNode(2)
    root.right  = TreeNode(3)
    root.left.right  = TreeNode(5)
    root.left.left  = TreeNode(4)


    print(f"Pre order Travers: {preOrder(root)}")
    print(f"Pre order Travers: {inOrder(root)}")
    print(f"Pre order Travers: {postOrder(root)}")

