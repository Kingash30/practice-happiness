class Node:
    def __init__(self, val):
        self.val=val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        self.head = newNode
    
    def print_middle_element(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next    #slow pointer moves one node
            fast = fast.next.next   #fast pointer moves two nodes
        print("\n\nThe middle element is ", slow.val)
    def Print_the_LL(self):
        temp = self.head
        if(temp!=None):
            print("The linked list elements are: ", end = " ")
            while (temp!=None):
                print(temp.val, end=" ")
                temp = temp.next
        else:
            print("The list is empty.")
newList = LinkedList()
newList.insert_at_the_beginning(5)
newList.insert_at_the_beginning(4)
newList.insert_at_the_beginning(3)
newList.insert_at_the_beginning(2)
newList.insert_at_the_beginning(1)
newList.Print_the_LL()
newList.print_middle_element()