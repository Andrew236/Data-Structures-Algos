class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self. nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
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

    def print_list(self):
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                print(currentNode.value)
                break
            else:
                print(currentNode.value)
                currentNode = currentNode.nextNode
        print("none")


ll = LinkedList()
ll.insert("5")
ll.insert("8")
ll.insert("9")
ll.print_list()