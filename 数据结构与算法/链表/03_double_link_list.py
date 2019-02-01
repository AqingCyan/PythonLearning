class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head = node  # 链表私有的属性，应该存的是头节点的地址，指向头节点，如果我们不传入节点，那就默认它是空，即空链表

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None  # 若为空则返回true

    def length(self):
        """链表长度"""
        # cur游标，用来遍历节点
        cur = self.__head  # 让游标指向起始节点
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next  # 让游标往后移动
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head  # 让游标指向起始节点
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next  # 打印完后移动游标
        print()

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)  # 创建节点
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head  # 让新节点的next指向原链表的头节点
            self.__head = node  # 让原链表的__head指向新节点
            node.next.prev = node  # 让头节点的p指针指向新节点

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)  # 构造节点
        if self.is_empty():  # 如果是空链表，就让头节点直接指向第一个节点
            self.__head = node
        else:
            cur = self.__head  # 让游标指向起始节点
            while cur.next is not None:  # 让游标移到尾节点，这里的判断条件是cur.next是为让游标移到尾节点就停止，而不是判空来结束遍历
                cur = cur.next
            cur.next = node  # 让尾节点的next指向新节点
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos: 插入位置，从0开始索引
        :param item: 待插节点
        """
        if pos < 0:  # 若传入的pos小于0，那认为要进行头插
            self.add(item)
        elif pos > (self.length() - 1):  # 若传入的pos比当前链表长，那我们就尾插
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0  # 这个count用来控制pre移动
            while count < pos:  # 让pre移动（指向）到指定的位置
                count += 1
                cur = cur.next
            # 当循环退出后
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """
        删除节点，只删除找到的第一个节点
        :param item: 要删除的节点
        """
        cur = self.__head
        while cur is not None:
            if cur.elem is item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur is self.__head:
                    self.__head = cur.next  # 让头节点指向第一个节点的下一个节点
                    if cur.next is not None:  # 判断链表是否只有一个节点
                        cur.next.prev = None
                    break
                else:
                    cur.prev.next = cur.next
                    if cur.next:  # 如果不是尾节点
                        cur.next.prev = cur.prev
                    break
            else:  # 如果不是要删除的节点，pre指向cur（往后移动一个节点），cur指向next（往后移动一个节点）
                pre = cur
                cur = cur.next

    def search(self, item):
        """
        查找节点是否存在
        :param item: 要查找的节点
        :return: 存在返回True，不在返回False
        """
        cur = self.__head  # 让游标指向头节点
        while cur is not None:  # 若游标指向的节点是None，就说明节点走完了
            if cur.elem is item:
                return True
            else:
                cur = cur.next
        return False  # 若未找到节点，就返回False

if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.add(0)
    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    dll.travel()

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.travel()
    # 8 0 1 2 3 4 5 6
    dll.insert(-1, 9)
    dll.travel()  # 9 8 0 1 2 3 4 5 6
    dll.insert(2, 100)
    dll.travel()  # 9 8 100 0 1 2 3 4 5 6
    dll.insert(10, 200)  # 9 8 100 0 1 2 3 4 5 6 200
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove(200)
    dll.travel()
    dll.add("23")
    dll.travel()