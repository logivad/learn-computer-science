from node import Node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list_rec(self):
    def print_node_value(node):
      node_value = node.get_value()
      next_node = node.get_next_node()

      if next_node:
        return str(node_value) + "\n" + print_node_value(next_node)
      else:
        return str(node_value)

    return print_node_value(self.head_node)

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node

    while current_node:
      string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()

    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.head_node

    if self.head_node.get_value() == value_to_remove:
      self.head_node = self.head_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()

        if next_node and next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
      

ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list().split("\n"))
ll.remove_node(55)
print(ll.stringify_list().split("\n"))
