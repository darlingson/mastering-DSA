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
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node
    def remove(self, key ):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
            else:
                previous = current
                current = current.next_node
        return current
    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Return the node or None if not found

        Time complexity: O(n)
        '''

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
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
    

# aa Test
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l)


# search Test
l2 = LinkedList()
l2.add(10)
l2.add(20)
l2.add(30)
l2.add(45)
print(l2.search(30))
print(l2.search(40))
print(l2.search(45))
print(l2)