class stack:
    def __init__(self):
        self.s = []
    
    def push(self, value):
        self.s.append(value)
    
    def pop(self):
        if self.is_Empty():
            return None
        else:
            return self.s.pop()
    
    def is_Empty(self):
        return len(self.s) == 0
    
    def top(self):
        if self.is_Empty():
            print("the stack is empty")
            return None
        else:
            return self.s[-1]