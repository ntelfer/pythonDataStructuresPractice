from stack import Stack


class StackQueue:

    def __init__(self):
        self.popStack = Stack.Stack()
        self.pushStack = Stack.Stack()

    def push(self, value):
        if self.pushStack.length() > 0:
            self.pushStack.push(value)
        else:
            # self.transfer(self.popStack, self.pushStack)
            self.pushStack.push(value)

    def pop(self):
        if self.popStack.length() > 0:
            return self.popStack.pop()
        else:
            self.transfer(self.pushStack, self.popStack)
            return self.popStack.pop()

    def transfer(self, fromStack, toStack):
        for x in range(fromStack.length()):
            toStack.push(fromStack.pop())
