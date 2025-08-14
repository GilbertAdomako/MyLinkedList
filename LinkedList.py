class Node():

    def __init__(self,data=None):
        self.data = data 
        self.next = None

class Linketlist():
    def __init__(self):
        self.head = Node()
        self.size = 0
        self.tail = self.head 

    def clear(self):
        self.head = Node()
        self.size= 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add(self, data, index ):
        new_node= Node(data)
        cur_index = 0
        current= self.head
        
        if data is None or index < 0 or index > self.size:
            print( "Error: Invalid Index or Data")
            return None
        
        while cur_index < index:
            current = current.next
            cur_index += 1
        new_node.next= current.next
        current.next = new_node
        if current== self.tail:
            self.tail = new_node
        self.size += 1


    def length(self):
        count = 0
        current = self.head.next

        while current != None:
            current= current.next
            count += 1 
        return count
    
    def display(self):
        elements= []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)  

    def get(self,index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None
        current_index = 0
        current = self.head
        
        while True:
            current = current.next
            if current_index == index: return current.data
            current_index += 1

    def sort(self):
        swapped = True

        while swapped:
            swapped = False

            current= self.head
            nextnode= current.next

            while nextnode != None:
                if current.data != None and nextnode.data != None and current.data > nextnode.data:
                    current.data, nextnode.data = nextnode.data, current.data
                    swapped = True
                current = nextnode
                nextnode = nextnode.next
    
    def erase(self,index):
        if index >= self.size:
            print("Error: Index Out Of Range")
            return None
        current_index = 0
        current = self.head

        while True:
            last_node= current
            current = current.next
            if current_index == index:
                last_node.next = current.next
                return
            current_index += 1
            self.size -= 1  

    def indexof(self, data):
        cur_node= self.head.next
        x_data= data

        for i in range(self.size):
            if cur_node is not None and cur_node.data == x_data:
                return i
            if cur_node is not None:
                cur_node = cur_node.next
        return -1

    


mylist= Linketlist()


mylist.append(4)
mylist.append(6)
mylist.append(45)
mylist.append(13)
mylist.append(32)
mylist.append(89)
mylist.append(32)
mylist.sort()
mylist.display()
print(mylist.indexof(89))


