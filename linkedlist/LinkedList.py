class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None


class LinkedList:
    def  __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after_node_v1(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


    def insert_after_node_v2(self, prev_node_data, data):
        new_node = Node(data)

        prev_node = self.head
        while prev_node.next:
            if prev_node.data == prev_node_data:
                new_node.next = prev_node.next
                prev_node.next = new_node
                break
            else:
                prev_node = prev_node.next


    def delete_node(self, key):
        cur_node = self.head
        # If deletion at the head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            print("Node with key ", key + "is not present")
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 1
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)



        


        


        

    




llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.insert_after_node_v1(llist.head.next, "E")
llist.insert_after_node_v2("B", "E")
llist.print_list()
llist.delete_node("E")
llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))