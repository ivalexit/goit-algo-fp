class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

    # 1. Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Алгоритм сортування однозв'язного списку (сортування вставками)
    def insertion_sort(self):
        sorted_list = None  # Початок нового відсортованого списку
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    # Функція для вставки у відсортований список
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

   