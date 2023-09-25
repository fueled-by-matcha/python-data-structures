from node import Node

class Stack:

  def __init__(self, limit=1000):
    self.top_value = None
    self.limit = limit
    self.size = 0

  def peek(self):
    if not self.is_empty():
      return self.top_value.get_value()
    else:
      print("This stack is empty!")

  def push(self, value):
    if self.has_space() == True:
      item = Node(value)
      item.set_next_node(self.top_value)
      self.top_value = item
      self.size += 1
    else:
      print("This stack is full!")

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is empty!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0

  
