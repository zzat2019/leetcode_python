# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return
        # 取nums列表的中间下标值
        mid_index = len(nums) // 2
        pNode = TreeNode(nums[mid_index])
        pNode.left = self.sortedArrayToBST(nums[:mid_index])
        pNode.right = self.sortedArrayToBST(nums[mid_index + 1:])
        return pNode