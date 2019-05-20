class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for i in str:
            if i >='A' and i <='Z':
                i =chr(ord(i)+32)
            else:
                pass
            res +=i
        return res

     return str.lower()