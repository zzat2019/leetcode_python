class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        a = 0
        for i in S:
            if i in J:
                a += 1
        return a
