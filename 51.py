class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    if not root:
        return "None,"
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)


def deserialize(data):
    def helper(nodes):
        val = nodes.pop(0)
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    return helper(data.split(","))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

data = serialize(root)
print(data)
new_root = deserialize(data)
