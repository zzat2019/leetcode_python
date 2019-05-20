class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        a= 0
        b= ""
        c=""
        for i in S:
            if i == '(':
                a += 1
                b += '('
            else:
                a -= 1
                b += ')'
            if a==0:
                c += b[1:-1]
                b = ''
        return c
