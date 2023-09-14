class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class DoublyLinkedList:
  #constructor
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  # adds new head node by first checking for a present head node and then checking for tail node
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    if current_head is not None:
      current_head.set_prev_node(new_head) 
      new_head.set_next_node(current_head) 
    self.head_node = new_head
    if self.tail_node is None:
      self.tail_node = new_head
# adds new tail by first checking for head node and then setting tail node
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    if current_tail is not None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    self.tail_node = new_tail
    if self.head_node is None:
      self.head_node = new_tail

  # removes head node and sets new node
  def remove_head(self):
    # set removed head to head node
    removed_head = self.head_node
    #check for null head
    if removed_head == None:
      return None
    # set head to next node
    self.head_node = removed_head.get_next_node()
    #check that head node is still not null and set previous node to none
    if self.head_node is not None:
      self.head_node.set_prev_node(None)
    # remove tail if it was the head
    if removed_head == self.tail_node:
      self.remove_tail()
    # return value of removed head
    return removed_head.get_value()

  def remove_tail(self):
  # set removed tail
   removed_tail = self.tail_node 
  # check for null head
   if removed_tail == None:
    return None
  # set new tail and remove next node
   self.tail_node = removed_tail.get_prev_node()
   if self.tail_node != None:
     self.tail_node.set_next_node(None)
   # remove head if it is the same as tail
   if removed_tail == self.head_node:
      self.remove_head()
  # return value of removed tail
   return removed_tail.get_value()
