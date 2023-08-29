"""
linked_list.py의 개선 버전.
기존의 linked_list는 n번째 원소를 직접 접근하지 못하고, head에서 시작해 순서대로 찾아가는 방식.(이전 노드와 대상노드를 알아야함.)
after가 붙은 함수를 통해 대상 노드를 가리키는 이전 노드(previous_node)를 찾아 신규 노드를 추가하거나 기존 노드를 삭제하므로,
탐색의 범위가 1 더 작다.
"""

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.num_nodes = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def __repr__(self):
        if self.num_nodes == 0:
            return "List is Empty"
        
        s = ''
        current_node = self.head
        while current_node != None:
            s += repr(current_node.data)
            if current_node.next != None:
                s += "->"

            current_node = current_node.next

        return s


    def get_items(self):
        result = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            result.append(current_node.data)
            
        return result


    def get_nth_node(self, n_th):
        if n_th < 0 or n_th > self.num_nodes:
            return None

        i = 0
        curr = self.head
        while i < n_th:
            curr = curr.next
            i += 1

        return curr


    def add_after(self, previous_node, new_node):
        new_node.next = previous_node.next
        if previous_node.next is None:
            self.tail = new_node
        previous_node.next = new_node
        self.num_nodes += 1
        return True


    def add_node(self, new_node, n):
        if n < 1 or n > self.num_nodes + 1:
            return False

        if n != 1 and n == self.num_nodes + 1:
            previous_node = self.tail
        else:
            previous_node = self.get_nth_node(n - 1)
        return self.add_after(previous_node, new_node)


    def delete_after(self, previous_node):
        if previous_node.next == None:
            return None
        
        curr = previous_node.next
        previous_node.next = curr.next
        if previous_node.next == None:
            self.tail = previous_node

        self.num_nodes -= 1
        return curr.data
                
        
    def delete_node(self, n):
        if n < 1 or n > self.num_nodes:
            raise IndexError
            
        previous_node = self.get_nth_node(n - 1)
        data = self.delete_after(previous_node)
        return data


def solution(x):
    return 0