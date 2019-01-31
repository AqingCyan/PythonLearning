# coding:utf-8
class Node(object):
    """节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# node = Node(100)


class SingleLinkList(object):
    """单链表"""
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
        node.next = self.__head  # 让新节点的next指向原链表的头节点
        self.__head = node  # 让原链表的__head指向新节点

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
        cur = self.__head  # 使用两个游标，cur指向要删除的，pre指向被删除的前一个节点
        pre = None  # 若找到了要删除节点，就使pre的next指向cur的next，被删除的那一项就与该链表无关了
        while cur is not None:
            if cur.elem is item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur is self.__head:
                    self.__head = cur.next  # 让头节点指向第一个节点的下一个节点
                    break
                else:
                    pre.next = cur.next
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

# 测试
if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.add(0)
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
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

