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