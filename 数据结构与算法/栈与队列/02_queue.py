class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        return self.__list.pop(0)

    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """返回长度"""
        return len(self.__list)

    