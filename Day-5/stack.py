class stackelements:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.appen(data)
    def is_empty(self):
        return self.stack=={}
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print('stack underflow')
    def diplay(self):
        if not self.is_empty():
            for top in range(len(self.stack)-1,-1,-1):
            print(self,stack[top])
        else:
            print('stack is empty')
    def peek(self):
        if not selt.is_empty():
            print('the peek ele:',self.stack[-1])
        else:
            print('stack is empty')

obj=stackexample()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.peek()
obj.pop()
obj.pop()
onj.push(44)
obj.diplay()
