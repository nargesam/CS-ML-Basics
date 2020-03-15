# Fibb algo in various ways: 


class Solution():

    # simple recursion
    def fib_recur(self, n):
        if n <= 2:
            return 1
        return self.fib_recur(n-1) + self.fib_recur(n-2)

    #  recursion with memo
    def fib_memo(self, n):
        memo = {}

        def cache(n):
            if n <= 2:
                memo[n] =  1
            
            if n in memo:
                return memo[n]
            else:
                memo[n] = cache(n-1) + cache(n-2)
                return memo[n]
        return cache(n)
    
    #  recursion with memo
    def fib_tab(self, n):
        if n <= 2:
            return 1
        f1 = 1
        f2 = 1
        for i in range(1, n):
            f1, f2 = f2, f1 + f2
        return f1



if __name__ == "__main__":
    
    sol = Solution()
    print("FIb using recursion")
    print(sol.fib_recur(1))
    print(sol.fib_recur(2))
    print(sol.fib_recur(5))
    print(sol.fib_recur(7))
    
    print("======================")

    print("FIb using memoization")
    print(sol.fib_memo(1))
    print(sol.fib_memo(2))
    print(sol.fib_memo(5))
    print(sol.fib_memo(7))
    
    print("======================")

    print("FIb using Tabularization")
    print(sol.fib_tab(1))
    print(sol.fib_tab(2))
    print(sol.fib_tab(5))
    print(sol.fib_tab(7))


