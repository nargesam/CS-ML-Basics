"""
implement setOfStacks() if the  size of stack exceeds a certain size, 
new stack gets created. 
"""

# TODO: need to handle deleting substacks once they got empty

class setOfStacks():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def pop(self):
        return self.stack[-1].pop()
    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append([data])
        elif len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(data)
        else: 
            self.stack.append([data])
    
    def popAt(self, idx):
        return self.stack[idx].pop()

stacks = setOfStacks(2)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
print(stacks.stack)
print(stacks.popAt(2))
print(stacks.stack)

