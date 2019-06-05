# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
#
# 只有给定的树是单值二叉树时，才返回
# true；否则返回
# false。
#
#
#
# 示例
# 1：
#
#
#
# 输入：[1, 1, 1, 1, 1, null, 1]
# 输出：true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 深度优先搜索
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = []
        def dsf(node):
            if node:
                val.append(node.val)
                dsf(node.right)
                dsf(node.left)
        dsf(root)
        return len(set(val))==1

    class Solution(object):
        def isUnivalTree(self, root):
            left_correct = (not root.left or root.val == root.left.val
                            and self.isUnivalTree(root.left))
            right_correct = (not root.right or root.val == root.right.val
                             and self.isUnivalTree(root.right))
            return left_correct and right_correct
