from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def obtainValuesBFS(self, root):
        if not root:
            return []
        
        output = []
        queue = deque([root])

        while queue:
            leftmost = queue.popleft()

            if not leftmost:
                continue

            output.append(leftmost.val)
            queue.append(leftmost.left)
            queue.append(leftmost.right)

        return output



if __name__ == "__main__":
    solution = Solution()

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

    print(solution.obtainValuesBFS(root)) # 1, 2, 2, 3, 4, 4, 3


