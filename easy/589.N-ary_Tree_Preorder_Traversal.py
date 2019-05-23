# 给定一个
# # # N
# # # 叉树，返回其节点值的前序遍历。
# # #
# # # 例如，给定一个
# # # 3
# # # 叉树:
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # 返回其前序遍历: [1, 3, 5, 6, 2, 4]。

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        递归的方式
        result = []
        if root is None:
            return result
        result.append(root.val)
        for node in root.children:
            result.extend(self.preorder(node))

        return result
        '''
        '''遍历的方式'''
        result = []
        temp = []
        if root == None:
            return result

        temp.append(root)

        while temp:
            p = temp.pop()
            result.append(p.val)

            if p.children:
                for c in p.children[::-1]:
                    temp.append(c)

        return result