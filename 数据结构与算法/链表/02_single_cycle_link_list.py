# coding:utf-8
class Node(object):
    """节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# node = Node(100)


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node  # 链表私有的属性，应该存的是头节点的地址，指向头节点，如果我们不传入节点，那就默认它是空，即空链表
        if node:
            node.next = node  # node的next指向自身，即只有一个节点的循环单链表

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None  # 若为空则返回true

    def length(self):
        """链表长度"""
        if self.is_empty():  # 如果说链表为空，返回0
            return 0
        # cur游标，用来遍历节点
        cur = self.__head  # 让游标指向起始节点
        # count记录数量
        count = 1
        while cur.next is not self.__head:  # 当游标移回到头节点的时候停止移动
            # 与单链表判断条件不同，不能使用cur来判断，因为使用cur来判断会导致循环开始的时候，就跳过循环（因为它是个圈嘛！）
            count += 1
            cur = cur.next  # 让游标往后移动
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head  # 让游标指向起始节点
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next  # 打印完后移动游标
        # 退出循环了，cur指向的是尾节点，但尾节点的元素未打印，因此需要打印出来
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)  # 创建节点
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head: # 循环退出来的时候，cur指向的就是尾节点
                cur = cur.next
            node.next = self.__head  # 让新节点的next指向原链表的头节点
            self.__head = node  # 让原链表的__head指向新节点
            cur.next = self.__head  # 再让尾节点指向node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)  # 构造节点
        if self.is_empty():  # 如果是空链表
            self.__head = node
            node.next = node
        else:
            cur = self.__head  # 让游标指向起始节点
            while cur.next is not self.__head:  # 让游标移到尾节点
                cur = cur.next
            node.next = self.__head
            cur.next = node  # 让尾节点的next指向新节点

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
            pre = self.__head  # 定义游标pre指向头节点
            count = 0  # 这个count用来控制pre移动
            while count < (pos - 1):  # 让pre移动（指向）到指定的位置
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向pos-1的位置，也就是说我们要找到的要插入位置的前一个节点已经有了
            node.next = pre.next  # 让node的next指向pre的下一个节点
            pre.next = node  # 让pre指向的节点的next指向我们插入的node

    def remove(self, item):
        """
        删除节点，只删除找到的第一个节点
        :param item: 要删除的节点
        """
        if self.is_empty():
            return
        cur = self.__head  # 使用两个游标，cur指向要删除的，pre指向被删除的前一个节点
        pre = None  # 若找到了要删除节点，就使pre的next指向cur的next，被删除的那一项就与该链表无关了
        while cur.next is not self.__head:
            if cur.elem is item:
                # 先判断此节点是否是头节点
                if cur is self.__head:
                    # 头节点的情况
                    # 找尾节点
                    rear = self.__head  # rear是找尾节点的游标
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next  # 让头节点指向第一个节点的下一个节点
                    rear.next = self.__head  # 让尾节点指向新的头节点（即为下一个节点）
                    return
                else:
                    pre.next = cur.next
                    return
            else:  # 如果不是要删除的节点，pre指向cur（往后移动一个节点），cur指向next（往后移动一个节点）
                pre = cur
                cur = cur.next
        # 退出循环，我们依然要处理尾节点的情况：cur指向尾节点，但循环退出了
        if cur.elem is item:
            if cur is self.__head:  # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """
        查找节点是否存在
        :param item: 要查找的节点
        :return: 存在返回True，不在返回False
        """
        if self.is_empty():  # 对链表进行判空操作
            return False
        cur = self.__head  # 让游标指向头节点
        while cur.next is not self.__head:  # 若游标指向的节点是头节点的指针，就说明游标走到了尾节点
            if cur.elem is item:
                return True
            else:
                cur = cur.next
        # 由于循环判断会导致走到尾节点时直接退出循环，尾节点不会被进行判断，因此我们需要手动判断一下
        if cur.elem is item:
            return True
        return False  # 若未找到节点，就返回False

# 测试
if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.add(0)
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    # 8 0 1 2 3 4 5 6
    ll.insert(-1, 9)
    ll.travel()  # 9 8 0 1 2 3 4 5 6
    ll.insert(2, 100)
    ll.travel()  # 9 8 100 0 1 2 3 4 5 6
    ll.insert(10, 200)  # 9 8 100 0 1 2 3 4 5 6 200
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(200)
    ll.travel()