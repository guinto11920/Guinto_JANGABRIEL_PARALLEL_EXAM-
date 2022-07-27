class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
n = 0
sum = 0

def push(head_ref, new_data):
    global head

    new_node = Node(0)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    head = head_ref


def sumOfLastN_Nodes(head):
    global sum
    global n

    if (head == None):
        return

    sumOfLastN_Nodes(head.next)

    if (n > 0):

        sum = sum + head.data
        n = n - 1

def sumOfLastN_NodesUtil(head, n):
    global sum

    if (n <= 0):
        return 0

    sum = 0
    sumOfLastN_Nodes(head)
    return sum

head = None

push(head, 12)
push(head, 1)
push(head, 4)
push(head, 6)
push(head, 10)
push(head, 5)

n = 3
print("Sum of last ", n, " nodes = ", sumOfLastN_NodesUtil(head, n))
