from node import Node

class Queue:

  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

  def peek(self):
    if self.is_empty() == True:
      print("Nothing to see here!")
      return None
    return self.head.get_value()

  def get_size(self):
    return self.size

def has_space(self):
  if self.max_size == None:
    return True
  return self.max_size > self.get_size()

def is_empty(self):
  return self.get_size() == 0
  

