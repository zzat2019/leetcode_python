# 给定一个
# N
# 叉树，返回其节点值的后序遍历。
#
# 例如，给定一个
# 3
# 叉树:
#
#
#
#
#
#
#
# 返回其后序遍历: [5, 6, 3, 2, 4, 1].

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        '''
        # 递归的方式
        result.append(root.val)
        for n in root.children[::-1]:
            po = self.postorder(n)
            for p in po[::-1]:
                result.insert(0,p)
        '''

        # 迭代的方式
        temp = []
        temp.append(root)
        while temp:
            node = temp.pop()
            result.insert(0, node.val)
            if len(node.children) > 0:
                for n in node.children:
                    temp.append(n)

        return result