from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.num_nodes = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

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


    def get_nth_node(self, n):
        if n < 0 or n > self.num_nodes:
            return None

        if n > self.num_nodes // 2:
            i = 0
            current_node = self.tail
            while i < self.num_nodes - n + 1:
                current_node = current_node.prev
                i += 1
        else:
            i = 0
            current_node = self.head
            while i < n:
                current_node = current_node.next
                i += 1

        return current_node


    def get_items(self, reverse=False):
        items = []

        if not reverse:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next ## head는 dummy node이므로, data값이 없다. 따라서 다음 노드로 이동한 다음, append를 해야한다.
                items.append(current_node.data)
        else:
            current_node = self.tail
            while current_node.prev.prev:
                current_node = current_node.prev
                items.append(current_node.data)

        return items
    

    def insert_back(self, next_node, new_node): ## 주어진 next_node의 뒤에 new_node를 삽입하는 메서드.
        prev_node = next_node.prev ## next_node의 이전 노드(prev_node)를 명시함.
        
        new_node.prev = prev_node ## 새로 추가된 노드가 prev_node와 next_node를 가리키는 형태가 되고,
        new_node.next = next_node
        
        prev_node.next = new_node ## 기존의 prev_node의 next는 new_node를, next_node의 prev가 new_node를 가리키도록 설정한다.
        next_node.prev = new_node
        
        self.num_nodes += 1
        
        return True


    def insert_front(self, prev_node, new_node):
        next_node = prev_node.next

        new_node.prev = prev_node
        new_node.next = next_node
        
        prev_node.next = new_node
        next_node.prev = new_node
        self.num_nodes += 1

        return True


    def insertAt(self, n, new_node):
        if n < 1 or n > self.num_nodes + 1:
            return False

        prev_node = self.get_nth_node(n - 1)
        return self.insert_front(prev_node, new_node)
    

    def delete_front(self, prev_node):
        trg_node = prev_node.next ## prev가 가리키던 다음 노드. 삭제 대상.
        next_node = trg_node.next ## 삭제 대상이 가리키던 다음 노드.
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.num_nodes -= 1
        return trg_node.data
        
        
    def delete_back(self, next_node):
        trg_node = next_node.prev
        prev_node = trg_node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node
        
        self.num_nodes -= 1
        return trg_node.data


    def delete_node(self, n):
        if n < 1 or n > self.num_nodes:
            raise IndexError
            
        prev_node = self.get_nth_node(n-1)
        return self.delete_front(prev_node)
        
        """
        n + 1을 인자로 하여 get_nth_node() 을 호출할 것이고, self.num_nodes == n 이므로 통과하지만,
        next 는 None이다. 이 상태로 delete_before(None)을 호출하면 next.prev를 계산하려 하는데 next == None이다. 
        따라서 prev 라는 속성을 가지지 않아서 AttributeError 가 발생.
        """
        # next_node = self.getAt(pos+1)
        # return self.delete_before(next_node)


    def concat(self, L):
        if self.num_nodes != 0 or L.num_nodes != 0: ## L1, L2 중 하나가 비어있거나, 둘 다 비어있지 않은 경우는 True. 둘 다 비어있을 때는 False.
            ## L1은 비어있지 않고, L2는 비어있다고 가정.
            L1_last_node = self.tail.prev ## L1의 마지막 노드(tail의 prev_node)
            L2_first_node = L.head.next ## L2의 첫번째 노드(head의 next_node인데 비어있으므로 tail)
            
            L1_last_node.next = L2_first_node ## L1의 마지막 노드가 L2의 tail을 가리킨다.(next)
            L2_first_node.prev = L1_last_node ## L2의 tail은 L1의 마지막 노드를 가리킨다.(prev)
            self.tail = L.tail ## L1의 tail을 L2의 tail로 설정.

            """ 반대로 L1이 비어있고 L2가 비어있지 않을 때.
            L1_last_node = self.tail.prev       ## L1의 마지막 노드(tail의 prev_node는 head)
            L2_first_node = L.head.next         ## L2의 첫번째 노드(head의 next_node 첫번째 노드)
            
            L1_last_node.next = L2_first_node   ## L1의 마지막 노드가(head.next) L2의 첫번째 노드를 가리킨다.
            L2_first_node.prev = L1_last_node   ## L2의 첫번째 노드는 L1(node.prev)의 마지막 노드(head)를 가리킨다.
            self.tail = L.tail ## L1의 tail을 L2의 tail로 설정.
            """
            
            self.num_nodes += L.num_nodes
            del(L)