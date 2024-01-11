class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({val!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({val!r}, {left!r})'
        else:
            fmt = '{}({val!r})'
        return fmt.format(type(self).__name__, **vars(self))


def build_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    while i < len(nums):
        current = queue.pop(0)

        if i < len(nums):
            current.left = TreeNode(nums[i])
            if current.left.val is not None:
                queue.append(current.left)
            i += 1

        if i < len(nums):
            current.right = TreeNode(nums[i])
            if current.right.val is not None:
                queue.append(current.right)
            i += 1

    return root


nums = [1, None, 2, None, 0, 3]
tree = build_tree(nums)
print(tree)
