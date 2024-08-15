class Node:
    def __init__(self, data=None):
        # Ініціалізація вузла списку. Кожен вузол містить дані та посилання на наступний вузол
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Ініціалізація порожнього списку. Початково голова (head) вказує на None
        self.head = None

    def insert_at_beginning(self, data):
        # Вставка нового вузла на початок списку
        new_node = Node(data)  # Створюємо новий вузол
        new_node.next = self.head  # Посилаємо новий вузол на поточну голову
        self.head = new_node  # Робимо новий вузол головою списку

    def insert_at_end(self, data):
        # Вставка нового вузла в кінець списку
        new_node = Node(data)  # Створюємо новий вузол
        if self.head is None:  # Якщо список порожній, новий вузол стає головою
            self.head = new_node
        else:
            cur = self.head  # Починаємо з голови
            while cur.next:  # Проходимо до кінця списку
                cur = cur.next
            cur.next = new_node  # Додаємо новий вузол у кінець списку

    def insert_after(self, prev_node: Node, data):
        # Вставка нового вузла після вказаного вузла
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створюємо новий вузол
        new_node.next = prev_node.next  # Новий вузол посилається на вузол після попереднього
        prev_node.next = new_node  # Попередній вузол тепер посилається на новий вузол

    def delete_node(self, key: int):
        # Видалення вузла з певним значенням (key)
        cur = self.head
        if cur and cur.data == key:  # Якщо голова містить потрібне значення
            self.head = cur.next  # Голова змінюється на наступний вузол
            cur = None  # Видаляємо вузол
            return
        prev = None
        while cur and cur.data != key:  # Проходимо список до знаходження потрібного вузла
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо не знайшли вузол, нічого не робимо
            return
        prev.next = cur.next  # Пропускаємо вузол, видаляючи його з ланцюжка
        cur = None  # Видаляємо вузол

    def search_element(self, data: int) -> Node | None:
        # Пошук вузла з певним значенням у списку
        cur = self.head
        while cur:
            if cur.data == data:  # Якщо знайшли потрібний вузол, повертаємо його
                return cur
            cur = cur.next
        return None  # Якщо не знайшли, повертаємо None

    def print_list(self):
        # Друк елементів списку
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')  # Вказуємо кінець списку

    def reverse(self):
        # Метод реверсування списку
        prev = None  # Початково попередній вузол - None
        current = self.head  # Починаємо з голови
        while current is not None:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev  # Змінюємо посилання поточного вузла на попередній
            prev = current  # Рухаємо попередній вузол вперед
            current = next_node  # Рухаємо поточний вузол вперед
        self.head = prev  # Голова тепер вказує на новий перший вузол (колишній останній)

    def merge_sort(self, head):
        # Метод сортування списку методом злиття
        if head is None or head.next is None:
            return head  # Якщо список порожній або має один елемент, він уже відсортований

        middle = self.get_middle(head)  # Знаходимо середній елемент списку
        next_to_middle = middle.next  # Другу половину починаємо з елемента після середнього
        middle.next = None  # Розділяємо список на дві частини

        left = self.merge_sort(head)  # Рекурсивно сортуємо ліву частину
        right = self.merge_sort(next_to_middle)  # Рекурсивно сортуємо праву частину

        sorted_list = self.sorted_merge(left, right)  # Зливаємо дві відсортовані частини
        return sorted_list

    def get_middle(self, head):
        # Метод знаходження середнього елемента списку
        if head is None:
            return head

        slow = head  # Повільний вказівник рухається по одному кроку
        fast = head  # Швидкий вказівник рухається по два кроки

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next  # Рухаємо повільний вказівник
            fast = fast.next.next  # Рухаємо швидкий вказівник

        return slow  # Повільний вказівник буде в середині списку

    def sorted_merge(self, a, b):
        # Метод злиття двох відсортованих списків
        if a is None:
            return b  # Якщо перший список порожній, повертаємо другий
        if b is None:
            return a  # Якщо другий список порожній, повертаємо перший

        if a.data <= b.data:  # Якщо значення першого списку менше або дорівнює
            result = a
            result.next = self.sorted_merge(a.next, b)  # Рекурсивно зливаємо залишок
        else:  # Якщо значення другого списку менше
            result = b
            result.next = self.sorted_merge(a, b.next)  # Рекурсивно зливаємо залишок

        return result

    def merge_sorted_lists(self, list1, list2):
        # Метод об'єднання двох відсортованих списків
        dummy = Node(0)  # Створюємо допоміжний вузол
        tail = dummy  # Початково хвіст вказує на допоміжний вузол

        p1 = list1.head  # Вказівник на голову першого списку
        p2 = list2.head  # Вказівник на голову другого списку

        while p1 is not None and p2 is not None:
            if p1.data <= p2.data:  # Додаємо менший елемент до нового списку
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next  # Рухаємо хвіст нового списку вперед

        if p1 is not None:  # Додаємо залишки першого списку, якщо такі є
            tail.next = p1
        if p2 is not None:  # Додаємо залишки другого списку, якщо такі є
            tail.next = p2

        return dummy.next  # Повертаємо голову злитого списку (пропускаючи допоміжний вузол)


if __name__ == '__main__':

    # Створюємо перший список
    first_list = LinkedList()
    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    # Реверсуємо перший список
    first_list.reverse()
    print("Зв'язний список після реверсування:")
    first_list.print_list()

    # Сортуємо перший список
    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список після сортування:")
    first_list.print_list()

    # Створюємо другий список
    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(20)
    second_list.insert_at_beginning(35)

    # Сортуємо другий список
    second_list.head = second_list.merge_sort(second_list.head)

    # Об'єднуємо два відсортованих списки
    merged_list_head = first_list.merge_sorted_lists(first_list, second_list)
    merged_list = LinkedList()
    merged_list.head = merged_list_head

    # Виводимо злитий список
    print("Зв'язний список після об'єднання двох відсортованих списків:")
    merged_list.print_list()
