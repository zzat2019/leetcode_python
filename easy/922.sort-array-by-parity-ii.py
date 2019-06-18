class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        res = [0]*len(A)
        res[::2] = even
        res[1::2] = odd
        return res

    class Solution(object):
        def sortArrayByParityII(self, A):
            """
            :type A: List[int]
            :rtype: List[int]
            """
            o = []
            j = []
            i = 0
            while i < len(A):
                if i % 2 == 0 and A[i] % 2 == 1:
                    j.append(i)
                elif i % 2 == 1 and A[i] % 2 == 0:
                    o.append(i)
                if len(j) > 0 and len(o) > 0:
                    n1 = j.pop()
                    n2 = o.pop()
                    A[n1], A[n2] = A[n2], A[n1]
                i += 1
            return A

