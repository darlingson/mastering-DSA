class Node:
    '''
    An object for storing a single node in a linked list
    Models two attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    '''
    Singly linked list
    ''' 
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        '''
        Returns the number of nodes in the list
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    def add(self, data):
        '''
        Adds a new node containing data at the head of the list
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                previous.next_node = current.next_node
                current.next_node = None
            previous = current
            current = current.next_node
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)
    

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)