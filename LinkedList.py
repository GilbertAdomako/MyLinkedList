class Node():

    def __init__(self,data=None):
        self.data = data 
        self.next = None

class Linketlist():
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_data= Node(data)
        current = self.head 
        while current.next != None:
            current= current.next
        current.next= new_data

    def length(self):
        count = 0
        current = self.head

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
            


my_list= Linketlist()
my_list.append(8)
my_list.append(23)
my_list.append(21)
my_list.append(43)
my_list.append(100)
my_list.append(53)
my_list.append(84)
my_list.append(12)
my_list.append(76)
my_list.append(1)


my_list.sort()
my_list.display()





    

    


