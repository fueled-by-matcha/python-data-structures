class LinkedList:
# constructor creates head node as a Node
	def __init__(self, value = None):
		self.head_node = Node(value)

	def get_head_node(self):
		return self.head_node

# insert a head node by creating a new node, linking it to old head, and setting new node to be head node
	def insert_beginning(self, new_value):
		new_node = Node(new_value)
		new_node.set_next_node(self.head_node)
		self.head_node = new_node

# convert linked list to string by starting with head node and traversing the list in a while loop
	def __repr__(self):
		node = self.head_node
		node_list = “”
		while node is not None:
			node_list += str(node.get_value()) + “\n”
			node = node.get_next_node()
		return node_list

# remove node method first checks head node for value to remove, then traverses the list starting with the next node checking for the value to remove
	def remove_node(self, value_to_remove):
    		current_node = self.head_node
   		 if current_node.get_value() == value_to_remove:
      			self.head_node = current_node.get_next_node()
   		 else:
      			while current_node is not None:
        				next_node = current_node.get_next_node()
       				 if next_node.get_value() == value_to_remove:
          					current_node.set_next_node(next_node.get_next_node()) 
          					current_node = None
       				 else:
          					current_node = next_node
