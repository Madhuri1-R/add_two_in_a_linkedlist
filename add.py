class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
def add_two_numbers(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.data
            l1 = l1.next
        if l2:
            total += l2.data
            l2 = l2.next
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
    return dummy.next
def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
ll1 = LinkedList()
n1 = int(input("Enter number of digits in first number: "))
for i in range(n1):
    num = int(input("Enter digit: "))
    ll1.insert(num)
ll2 = LinkedList()
n2 = int(input("Enter number of digits in second number: "))
for i in range(n2):
    num = int(input("Enter digit: "))
    ll2.insert(num)
result = add_two_numbers(ll1.head, ll2.head)
print("Result Linked List:")
display(result)