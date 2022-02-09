"""
پالیندروم بودن یک لیست پیوندی را به 3 روش میتوان انجام داد:
1- استفاده از پشته
2- روش معکوس کردن
3- روش تو در تو(از چپ و راست لیست 2 نشانه گر را مأمور بررسی میکنیم)
ما در اینجا از روش دوم یعنی معکوس کردن لیست استفاده کردیم
به این صورت که لیست را از وسط نصف میکنیم و با معکوس کردن کنترل میکنیم که آیا مقادیر یک قسمت با مقادیر قسمت دیگر برابر است یا خیر و به این صورت اگر تمام مقادیر با هم برابر بودند مشخص می شود که لیست ما پالیندروم است
توابع درون کلاسها مشخص شده اند
"""


# کلاس گره
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# کلاس لیست پیوندی
class LinkedList:

    def __init__(self):
        self.head = None

    # چک کردن پالیندورم بودن مقادیر لیست پیوندی
    def isPalindrome(self, head):

        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head

        midnode = None

        res = True

        if head is not None and head.next is not None:

            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next

            if fast_ptr is not None:
                midnode = slow_ptr
                slow_ptr = slow_ptr.next

            second_half = slow_ptr

            prev_of_slow_ptr.next = None

            second_half = self.reverse(second_half)

            res = self.compareLists(head, second_half)

            second_half = self.reverse(second_half)

            if midnode is not None:

                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res

    # تابع معکوس کردن لیست پیوندی
    def reverse(self, second_half):

        prev = None
        current = second_half
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        second_half = prev
        return second_half

    # مقایسه این که دو بخش لیست آیا مقدار مساوی دارند یا خیر؟
    def compareLists(self, head1, head2):

        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0

        if temp1 is None and temp2 is None:
            return 1

        return 0

    # تابع افزودن به ابتدای لیست
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    # تابع چاپ لیست
    def printList(self):

        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("خالی")


# اجرای کد
if __name__ == '__main__':

    linkedlist = LinkedList()
    s = [1, 2, 1, 3, 1, 2, 1]

    for i in range(7):
        linkedlist.push(s[i])
        linkedlist.printList()

        if linkedlist.isPalindrome(linkedlist.head):
            print("پالیندروم است\n")
        else:
            print("پالیندروم نیست\n")
        print()
