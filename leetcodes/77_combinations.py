class Solution:
    def combine(self, n, k):
        
        if k == 0:
            return [[]]
        # return [pre + [i] for i  in range(k, n+1) for pre in self.combine(i-1, k-1)]
        
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1 )]
        return combs
            
        
n = 3
k = 2

sol = Solution()
print(sol.combine(n,k))