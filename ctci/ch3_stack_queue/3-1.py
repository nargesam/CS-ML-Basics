"""
implement three stacks using one array 

"""

class kstackWithArray():
    def __init__(self, k, n):
        self.ssize = n//k
        self.size = n
        self.arr = [None]*n
        # starting point for the k stacks
        self.tops = [0,0,0]
    
    def push(self, data, sn):
        if not self.isFull(sn):
            self.arr[ sn*self.ssize + self.tops[sn]] = data 
            self.tops[sn] += 1
        else:
            print(f"stack overflow: stack {sn} is full")
    
    def pop(self, sn):
        topop = self.arr[sn*self.ssize +self.tops[sn]]
        self.arr[sn*self.ssize +self.tops[sn] -1] = None
        self.tops[sn] -= 1
        return topop
    
    def isFull(self, sn):
        if sn*self.ssize + self.tops[sn] == self.size-1 or sn*self.ssize + self.tops[sn] == (sn+1)*self.ssize:
            return True
        else: 
            return False

stack = kstackWithArray(3, 10)
stack.push(100, 0)
stack.push(200, 1)
stack.push(300, 2)
stack.push(100, 0)
stack.push(100, 0)
stack.push(100, 0)
print(stack.arr)






