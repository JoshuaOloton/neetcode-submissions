class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        if not self.head:
            return -1
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
            if not temp:
                return -1
        
        return temp.data
        

    def insertHead(self, val: int) -> None:
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
            return
        n.next = self.head
        self.head = n
        

    def insertTail(self, val: int) -> None:
        n = Node(val)
        if not self.tail:
            self.tail = n
            self.head = n
            return
        self.tail.next = n
        self.tail = n
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index-1):
                if temp.next:
                    temp = temp.next
                else:
                    return False
            if not temp.next:
                return False
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        return arr
        
