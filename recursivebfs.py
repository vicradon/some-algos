# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_bfs(queue, output):
    if not queue:
        return
    
    new_queue = []
    for node in queue:
        if not node:
            continue

        output.append(node.val)

        new_queue.append(node.left)
        new_queue.append(node.right)

    recursive_bfs(new_queue, output)



if __name__ == "__main__":
    # Example 1
    #      1
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    queue = [root]
    output = []

    recursive_bfs(queue, output)
    print(output) # 1, 2, 2, 3, 4, 4, 3

