迭代36ms

class Solution:
    def fib(self, N: int) -> int:
        i=0
        j=1
        while N:
            N-=1
            i,j=j,j+i
        return i
递归

class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        return self.fib(N-1)+self.fib(N-2)