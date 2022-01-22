class stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return self.stack==[]
    def push(self,element):
        self.stack.append(element)
        print("{0} element is pushed".format(element))
    def pop(self):
        if not self.is_empty():
            self.poped_element=self.stack.pop()
            print("poped {0} element from the stack".format(self.poped_element))
        else:
            print("stack is empty")
    def size(self):
        print(len(self.stack))    
    def display(self):
        print("The elements in the stack are")
        for i in self.stack:
            print(i,end=" ,")
        print("\n")
    def peek(self):
        if not self.is_empty():
            print("peek element is {0}".format(self.stack[-1]))
        else:
            print("Empty stack")    
         
mystack= stack()
mystack.push(9)
mystack.push(4)
mystack.push(94)
mystack.push(92)
mystack.pop()
mystack.size()
mystack.display()
mystack.peek()