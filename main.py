# 1
# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.next = new_node

    def delete(self, data):
        current = self.head
        prev = None

        while current is not None:
            if current.data == data:
                if prev is not None:
                    prev.next = current.next
                else:
                    self.head = current.next
                return

            prev = current
            current = current.next

    def is_in_list(self, value):
        current_value = self.head
        while current_value:
            if current_value.data == value:
                return True
            else:
                return False


    def replace(self, current_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.data == current_value:
                current_node.data = new_value
            current_node = current_node.next

my_list = LinkedList()
for i in range(5):
    num = int(input("Input number: "))
    my_list.append(num)

my_list.append(4)

my_list.delete(3)

print(my_list.is_in_list(22))

my_list.replace(2, 6)

print(my_list)













