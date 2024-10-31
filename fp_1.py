import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, sorted_head, new_node):
        if not sorted_head or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_head

    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = LinkedList()
        p1, p2 = list1.head, list2.head

        while p1 and p2:
            if p1.data <= p2.data:
                merged_list.insert_at_end(p1.data)
                p1 = p1.next
            else:
                merged_list.insert_at_end(p2.data)
                p2 = p2.next

        while p1:
            merged_list.insert_at_end(p1.data)
            p1 = p1.next
        while p2:
            merged_list.insert_at_end(p2.data)
            p2 = p2.next

        return merged_list

# Створення списку з 10 унікальними випадковими числами в межах 1-100
llist = LinkedList()
unique_random_numbers = random.sample(range(1, 101), 10)

for number in unique_random_numbers:
    llist.insert_at_end(number)

print("Generated list:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("\nList after reversal:")
llist.print_list()

# Сортування списку
llist.insertion_sort()
print("\nList after sorting:")
llist.print_list()