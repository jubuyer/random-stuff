# -*- coding: utf-8 -*-
"""Single_linked_list_ja.ipynb
### Singly-linked list (SLL)

Create an SLL class that will implement a singly-linked list to be used as a stack (last-in first-out).

Use the Node class below as nodes carrying data in the SLL.

Implement all of the methods that are awaiting your excellent code in the SLL note below.  Remove the Python "pass" command in each method, replacing with with your own code.
"""

class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
        
  def value(self):
    return self.data

class SLL:

  # if data_list is provided, it must be a list of values, and they are pushed one-by-one onto SLL
  def __init__(self,data_list = None):
    self.head = None
    self.current = None
    self.size = 0 
    n = len(data_list)
    for i in range(0,n):
      a = data_list[i]
      self.push(a)
    

  # adds a Node with data to the front of SLL, assume data is not None
  def push(self,data):
    node = Node(data)
    if self.head:
      node.next = self.head
    self.head = node
    self.size += 1

  # If SLL is empty, returns None.  Else returns the data of the first Node, and removes the Node.
  def pop(self):
    if self.head is None:
      return None
    info = self.head.value()
    self.head = self.head.next
    self.size -= 1
    return info

  # returns the data from the first Node, makes the first Node "current", else None if SLL is empty
  def getFirst(self):
    if self.head is None:
      return None
    self.current = self.head
    return self.current.value()
    
  # moves internally to the Node after "current" (if possible), and returns its data, else None
  #  cannot be used after push() or pop() calls, only after getFirst() or getNext()
  def getNext(self):
    if self.current.next is None:
      return None
    self.current = self.current.next
    return self.current.value()

  # returns number of Nodes in SLL
  def length(self):
    return self.size

  # empties SLL, returns None
  def clear(self):
    self.head = None    
    return None

# Test...

input = [4,7,2,2,1,8]
a = SLL(input)

def forward(a):
  # use getFirst() and getNext() to acquire the list
  fwd = []
  d = a.getFirst()
  if d:
    fwd.append(d)
  d = a.getNext()
  while d:
    fwd.append(d)
    d = a.getNext()
  return fwd

def back(a):
  # use pop() to acquire the list
  bk = []
  d = a.pop()
  while d:
    bk.append(d)
    d = a.pop()
  return bk 

# Make sure that both lists are the same, and they are the reverse of the input list
fwd = forward(a)
bk = back(a)
if fwd == bk and fwd == input[::-1]:
  print('Success!')
else:
  print('Nope.  A problem...')
print(fwd)
print(bk)
