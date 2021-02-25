#stacks and queues implementation
#showing multiple ways for queues

from collections import deque

#implementing a stack.. stacks are built off arrays so the implementation will be using an array
#to uphold the integrity of a stack I will only use append, and pop

stack = []
stack.append("andrew")
stack.append("cole")
stack.pop()
print(stack)


#Implementing a queue with the deque library
data = deque()
data.append("andrew")
element = data.popleft()
print(element, data)


#implementing stacks/queues with custom classes
#stack implementation
#complexity insertion is an amortized O(1) deletion is O(1) time
#traversal is O(1)
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        if len(self.data) == 0:
            return
        else:
            self.data.remove(self.data[len(self.data) - 1])

    def print_stack(self):
        print(self.data)

stack1 = Stack()
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.pop()
stack1.print_stack()


#queue implementation
#runtime for queue/deque is 0(1) time/space
#fining element/traversal is O(n)
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class Queue:
    def __init__(self,head=None):
        self.head = head

    def enque(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode == None:
                    currentNode.nextNode = node
                    break
                else:
                    currentNode = currentNode.nextNode

    def deque(self):
        if self.head == None:
            return
        else:
            currentNode = self.head
            self.head = currentNode.nextNode



    def traverse(self):
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                print(currentNode.value)
                break
            else:
                print(currentNode.value)
                currentNode = currentNode.nextNode
        


q = Queue()
q.enque(3)
q.enque(4)
q.enque(5)
q.enque(6)
q.enque(7)
q.enque(8)
q.enque(9)
q.deque()
q.deque()
q.deque()
q.deque()
q.traverse()


        

