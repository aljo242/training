
class Node:
    """
    Object for storing a single node of a singly linked list
    Models two attributes: data and the link to the next node in list
    """

    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"

class LinkedList:
    """
    Singly linked list
    """

    head = None
    size = 0

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        """
        returns a string representation of the list
        Takes O(n) time
        """
        nodes= []
        n = self.head
        while n != None:
            if n == self.head:
                nodes.append(f"[Head: {n.data}]")
            elif n.next == None:
                nodes.append(f"[Tail: {n.data}]")
            else:
                nodes.append(f"[{n.data}]")

            n = n.next

        return f"List:\n\tSize: {self.size}\n\t" + "-> ".join(nodes)

    def is_empty(self):
        return self.head == None

    def size(self):
       return self.size

    def prepend(self, data):
        """
        adds a new node to the HEAD of the list
        Takes O(1) time
        """
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp
        self.size += 1

    def append(self, data):
        """
        adds new node to the TAIL of the lsit
        Takes O(n) time (n = len(list))
        """
        # find end of the list
        n = self.head
        while n.next != None:
            n = n.next
        
        n.next = Node(data)
        self.size += 1


    def insert(self, data, index):
        """
        inserts data AFTER index
        if you want to add an element to the front of the list, use the PREPEND method
        """
        if index < 0:
            return
        else:
            n = self.head

            while index != 0:
                n = n.next
                if n == None:
                    return
                index -= 1

            tmp = n.next
            n.next = Node(data)
            n.next.next = tmp
            self.size += 1


    def removeValue(self, value):
        _, index = self.find(value)
        removeIndex(index)

        


    def removeIndex(self, index):
        if index > self.size-1  or index == -1:
            return

        n = self.head
        for i in range(index):
            n = n.next

        
        

    def find(self, value):
        """
        search for and return  the first node containing the data that matches the given value, else return None
        O(n) time
        """
        n = self.head
        index = 0
        while n != None:
            if n.data == value:
                return n, index

            n = n.next
            index += 1

        return None, -1


def main():
    print("Hi")
    
    l = LinkedList()
    print(l.is_empty())
    print(l)
    l.prepend(30)
    l.append(40)
    print(l)

    print(l.find(40))
    print(l.find(50) == None)
    print(l.is_empty())

    l.insert(5, 1)
    l.insert(5, 5)
    l.insert(5, -1)
    l.insert(1, 0)
    l.insert(3,2)
    print(l)

if __name__ == "__main__":
    main()