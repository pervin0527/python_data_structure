from node import Node
from doubly_linked_list import DoublyLinkedList

L1 = DoublyLinkedList()
a = Node(10)
b = Node(20)
c = Node(30)

L1.insertAt(1, a)
L1.insertAt(2, b)
L1.insertAt(3, c)

print(L1)

L2 = DoublyLinkedList()
L2.concat(L1)
print(L2)

L2.insertAt(2, Node(100))
print(L2)

for _ in range(L2.num_nodes):
    L2.delete_node(1)
    print(L2)