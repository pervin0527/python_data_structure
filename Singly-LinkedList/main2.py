from linked_list_ver2 import Node, LinkedList

L1 = LinkedList()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(100)

L1.add_node(a, 1)
L1.add_node(b, 2)
print(f"Total list : {L1}")
print(f"Get Items : {L1.get_items()}")

L1.add_node(c, 2)
print(f"Total list : {L1}")
L1.add_node(d, 3)
print(f"Total list : {L1}")

n_th_node = L1.get_nth_node(2)
print(f"Get n-th item : {n_th_node.data}, {n_th_node.next}")

print((L1.delete_node(1)))
print(f"Total list : {L1}")

print(L1.delete_node(1))
print(f"Total list : {L1}")
print(L1.delete_node(2))
print(f"Total list : {L1}")

L2 = LinkedList()
a = Node(10)
L2.add_node(a, 1)