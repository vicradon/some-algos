# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.checkSymmetry(root.left, root.right)
        
    def checkSymmetry(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        
        return (left.val == right.val) and self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left)


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

    print(solution.isSymmetric(root)) # True

