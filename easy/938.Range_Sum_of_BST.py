# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

# 二叉搜索树保证具有唯一的值。

 

# 示例 1：

# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.right, L, R) + self.rangeSumBST(root.left, L, R)

# 二叉搜索树左<根<右