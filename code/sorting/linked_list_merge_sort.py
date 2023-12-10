# from code.data_structures.linked_list import LinkedList
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
    
    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

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
    




def merge_sort(linked_list):
    """
    Sorts list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until the one remains

    Returns a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    '''
    Divide the unsorted list at midpoint into sublists
    '''

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half,right_half
    else :
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid -1)

        left_half = linked_list
        right_half = LinkedList()

        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half,right_half
    
def merge(left,right):

    merged = LinkedList()
    merged.add(0)
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node

            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    head = merged.head.next_node
    merged.head = head
    return merged


    
l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
