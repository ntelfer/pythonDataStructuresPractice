from stack import StackQueue


values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

myQueue = StackQueue.StackQueue()

for val in values:
    myQueue.push(val)

for x in range(len(values)):
    print(myQueue.pop())
