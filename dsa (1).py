#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sum1(ar,n,sum):
    count =0
    for i in range(n):
        for j in range(i+1,n):
            if ar[i]+ar[j]==sum:
                count+=1
    return count
n= int(input("enter the size of array"))
ar=[]
for i in range(n):
    ar.append(int(input()))
sum =int(input("enter the sum "))
print(sum1(ar,n,sum))


# In[5]:


arr = [1, 2, 3, 4, 5];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
print("Array in reverse order: ");    
   
for i in range(len(arr)-1, -1, -1):     
    print(arr[i]),  


# In[6]:



def areRotations(string1, string2):
	size1 = len(string1)
	size2 = len(string2)
	temp = ''

	if size1 != size2:
		return 0

	temp = string1 + string1


	if (temp.count(string2)> 0):
		return 1
	else:
		return 0


string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
	print ("Strings are rotations of each other")
else:
	print ("Strings are not rotations of each other")



# In[7]:



NO_OF_CHARS = 256


def getCharCountArray(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+= 1
	return count


def firstNonRepeating(string):
	count = getCharCountArray(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break
		k += 1

	return index

string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
	print ("Either all characters are repeating or string is empty")
else:
	print ("First non-repeating character is" , string[index])



# In[8]:




def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
		

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')


# In[1]:


# Class to make a Node
class Node:
	# Constructor which assign argument to nade's value
	def __init__(self, value):
		self.value = value
		self.next = None

	# This method returns the string representation of the object.
	def __str__(self):
		return "Node({})".format(self.value)
	
	# __repr__ is same as __str__
	__repr__ = __str__


class Stack:
	# Stack Constructor initialise top of stack and counter.
	def __init__(self):
		self.top = None
		self.count = 0
		self.minimum = None
		
	# This method returns the string representation of the object (stack).
	def __str__(self):
		temp = self.top
		out = []
		while temp:
			out.append(str(temp.value))
			temp = temp.next
		out = '\n'.join(out)
		return ('Top {} \n\nStack :\n{}'.format(self.top,out))
		
	# __repr__ is same as __str__
	__repr__=__str__
	
	# This method is used to get minimum element of stack
	def getMin(self):
		if self.top is None:
			return "Stack is empty"
		else:
			print("Minimum Element in the stack is: {}" .format(self.minimum))



	# Method to check if Stack is Empty or not
	def isEmpty(self):
		# If top equals to None then stack is empty
		if self.top == None:
			return True
		else:
		# If top not equal to None then stack is empty
			return False

	# This method returns length of stack	
	def __len__(self):
		self.count = 0
		tempNode = self.top
		while tempNode:
			tempNode = tempNode.next
			self.count+=1
		return self.count

	# This method returns top of stack	
	def peek(self):
		if self.top is None:
			print ("Stack is empty")
		else:
			if self.top.value < self.minimum:
				print("Top Most Element is: {}" .format(self.minimum))
			else:
				print("Top Most Element is: {}" .format(self.top.value))

	# This method is used to add node to stack
	def push(self,value):
		if self.top is None:
			self.top = Node(value)
			self.minimum = value
		
		elif value < self.minimum:
			temp = (2 * value) - self.minimum
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.minimum = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}" .format(value))

	# This method is used to pop top of stack
	def pop(self):
		if self.top is None:
			print( "Stack is empty")
		else:
			removedNode = self.top.value
			self.top = self.top.next
			if removedNode < self.minimum:
				print ("Top Most Element Removed :{} " .format(self.minimum))
				self.minimum = ( ( 2 * self.minimum ) - removedNode )
			else:
				print ("Top Most Element Removed : {}" .format(removedNode))

				
			
	
# Driver program to test above class
stack = Stack()

stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()	
stack.pop()
stack.getMin()
stack.pop()
stack.peek()



# In[ ]:




