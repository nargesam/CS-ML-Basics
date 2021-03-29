""""
return push pop min in O(1)

"""


class minStack():
    def __init__(self):
        self.stack = []
        self.min = [float('INF')]

    def push(self, data): 
        if data < self.min[-1]: 
            self.min.append(data)
        else: 
            self.min.append(self.min[-1])
        self.stack.append(data)
    
    def pop(self):
        self.min.pop()
        return self.stack.pop()
    
    def retMin(self):
        return self.min[-1]
    
    def peek(self):
        return self.stack[-1]

stack = minStack()
stack.push(100)
stack.push(10)
stack.push(100)
stack.push(2)
print(stack.retMin())
print(stack.stack )
