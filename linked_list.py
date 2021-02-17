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
    
    def delete(self, value):
        currentNode = self.head
        if value == self.head.value:
            self.head = self.head.nextNode
            currentNode = None
            return
        else:
            prev_node = None
            while currentNode and currentNode.value != value:
                prev_node = currentNode
                currentNode = currentNode.nextNode
            
            if currentNode is None:
                print("Element to be deleted is not found")
            else:
                prev_node.nextNode = currentNode.nextNode
                currentNode = None





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
ll.insert("7")
ll.insert("9")

ll.delete("7")
ll.print_list()
