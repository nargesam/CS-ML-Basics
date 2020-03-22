# Count the number of prime numbers less than a non-negative number, n.
class Solution():
    def cntPrime(self, n):

        if n < 2:
            return 0
        
        strikes = [1]*n
        strikes[0] = 0
        strikes[1] = 0
#  the smallest factor of a non-prime number will not be > sqrt(n).
        # now go untill sqrt(n), and find all numbers that have not been processed yet
        # then change all of their multiples to zero since they won't be a prime num for sure 
        # then count the remaining 1s in the list

        for i in range(2, int(n**0.5) + 1):

            if strikes[i] != 0: 
                # [i*i:n:i]: from i*i to the end  of list, every i jump -> find all numbers
                # that i is the factor for them and set them to 0 (0 being not prime)
                strikes[i*i:n:i] = [0]*((n-1-i*i)//i + 1)
            
        return sum(strikes)


sol = Solution()
print(sol.cntPrime(10))