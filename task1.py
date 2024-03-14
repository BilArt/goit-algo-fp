class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted_lists(self, list1, list2):
        merged_list = LinkedList()
        while list1.head or list2.head:
            if not list1.head:
                merged_list.sorted_insert(list2.head)
                list2.head = list2.head.next
            elif not list2.head:
                merged_list.sorted_insert(list1.head)
                list1.head = list1.head.next
            elif list1.head.data < list2.head.data:
                merged_list.sorted_insert(list1.head)
                list1.head = list1.head.next
            else:
                merged_list.sorted_insert(list2.head)
                list2.head = list2.head.next
        return merged_list

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Приклад використання:
# Створення списку
linked_list = LinkedList()

# Додавання елементів
linked_list.sorted_insert(Node(5))
linked_list.sorted_insert(Node(3))
linked_list.sorted_insert(Node(7))
linked_list.sorted_insert(Node(1))

# Вивід вихідного списку
print("Вихідний список:")
linked_list.display()

# Реверсування списку
linked_list.reverse()
print("Реверсований список:")
linked_list.display()

# Створення та сортування другого списку
linked_list2 = LinkedList()
linked_list2.sorted_insert(Node(4))
linked_list2.sorted_insert(Node(2))
linked_list2.sorted_insert(Node(8))
linked_list2.sorted_insert(Node(6))
print("Сортований другий список:")
linked_list2.display()

# Об'єднання та сортування списків
merged_list = linked_list.merge_sorted_lists(linked_list, linked_list2)
print("Об'єднаний та відсортований список:")
merged_list.display()
