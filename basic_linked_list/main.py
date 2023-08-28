from linked_list import Node, LinkedList

linked_list = LinkedList()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(100)

linked_list.add_node(a, 1)
linked_list.add_node(b, 2)
print(f"Total list : {linked_list}")
print(f"Get Items : {linked_list.get_items()}")

linked_list.add_node(c, 2)
print(f"Total list : {linked_list}")
linked_list.add_node(d, 3)
print(f"Total list : {linked_list}")

n_th_node = linked_list.get_nth_node(2)
print(f"Get n-th item : {n_th_node.data}, {n_th_node.next}")

print((linked_list.delete_node(1)))
print(f"Total list : {linked_list}")

print(linked_list.delete_node(1))
print(f"Total list : {linked_list}")
print(linked_list.delete_node(2))
print(f"Total list : {linked_list}")
print(linked_list.delete_node(1))
print(f"Total list : {linked_list}")