class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.num_nodes = 0
        self.head = None
        self.tail = None


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
        

    def get_nth_node(self, n_th):
        """
        n번째 노드를 가져오는 메서드.
        params
            n_th(int) : 찾고자 하는 Node의 번호.

        return
            Node(object) : idx번째 node
        """

        ## 잘못된 idx를 입력하거나, node 수보다 큰 값을 입력 했을 경우 False를 반환하고 종료.
        if n_th < 1 or n_th > self.num_nodes:
            return False
        
        ## 올바른 n_th 값이 입력되었으면, n번째 node를 찾는다.
        i = 1
        current_node = self.head ## 시작점(self.head)부터 n번째 노드를 순차적으로 찾아간다.
        while i < n_th:
            current_node = current_node.next
            i += 1

        return current_node
        

    def get_items(self):
        """
        연결리스트에 포함된 모든 node의 data를 list에 담아 반환하는 메서드.

        return
            items(list)
        """
        items = []

        ## get_nth와 마찬가지로 시작점에서부터 self.tail까지 순차적으로 찾아간다.
        current_node = self.head
        while current_node != None: ## tail은 마지막 노드이므로, 다음 노드가 없다. 따라서 None이면 iteration을 종료한다.
            items.append(current_node.data)
            current_node = current_node.next

        return items
    

    def add_node(self, new_node, idx):
        """
        연결리스트에 새로운 노드를 추가한다.
        params
            new_node : Node 객체.
            idx : new_node를 추가할 위치.

        return
            True or False
        """

        if idx < 1 or idx > self.num_nodes + 1: ## index 검사.
            return False
        
        if idx == 1: ## head 위치에 새로운 노드가 추가되는 경우.
            new_node.next = self.head ## 추가된 노드가 기존 head 노드를 가리킨다.
            self.head = new_node ## 추가된 노드를 head로 설정.

        else:
            if idx == self.num_nodes + 1: ## tail 위치에 새로운 노드가 추가되는 경우
                previous_node = self.tail ## tail이 이전 노드가 되고, 신규 노드를 가리킬 수 있도록 해야한다.
                
            else:
                previous_node = self.get_nth_node(idx - 1) ## head, tail이 아닌 중간 위치에 노드가 추가되는 경우, 해당 위치 이전의 노드를 가져와야 링크를 수정해야한다.
                
            new_node.next = previous_node.next ## 기존에 있던 노드의 연결이 새로 추가된 노드의 연결로 대체.
            previous_node.next = new_node ## 기존에 있던 노드는 새로운 노드를 연결한다.

        if idx == self.num_nodes + 1: ## 새로운 노드가 tail위치 일 경우
            self.tail = new_node ## 새롭게 tail을 지정해준다.


        self.num_nodes += 1
        return True


    def delete_node(self, idx):
        """
        n번째 노드를 삭제한다.
        params
            idx(int) : 삭제하고자 하는 위치 n번째.

        return
            data(int) : 삭제된 노드가 가지고 있던 값을 반환한다.
        """
        if idx < 1 or idx > self.num_nodes + 1: ## 입력된 index가 올바른 값인지 검사한다.
            raise IndexError
        
        if idx == 1: ## head 위치의 노드를 삭제하는 경우.
            current_node = self.head
            data = current_node.data ## head node가 가지고 있던 값을 별도의 변수에 저장.

            if self.num_nodes == 1: ## 현재 연결리스트에 노드가 하나만 있는 경우, 해당 노드가 삭제되기 때문에 head와 tail은 모두 None으로 설정.
                self.head = None
                self.tail = None
            
            self.head = current_node.next ## head가 가리키고 있던 다음 node를 head로 설정한다.

        else:
            i = 1
            current_node = self.head ## head 노드가 아닌 다른 위치의 노드를 삭제하려는 경우.
            while i < idx: ## 대상 노드를 찾는다.
                current_node = current_node.next
                i += 1
            
            data = current_node.data
            previous_node = self.get_nth_node(i - 1) ## 대상 노드의 이전 노드를 가져와서 링크들을 조정해야 한다.
            previous_node.next = current_node.next ## 이전 노드의 링크에 삭제 대상 노드가 가리키던 노드를 담는다.

            if idx == self.num_nodes: ## tail 노드가 삭제되는 경우.
                self.tail = previous_node ## tail을 가리키던 노드를 tail로 설정한다.

        self.num_nodes -= 1
        return data
    

    def concat(self, L):
        """
        인자로 전달된 연결 리스트 객체를 현재 객체에 연결.
        """
        self.tail.next = L.head
        if L.tail: ## L이 비어있는 리스트가 아닌 경우,
            self.tail = L.tail

        self.num_nodes += L.num_nodes