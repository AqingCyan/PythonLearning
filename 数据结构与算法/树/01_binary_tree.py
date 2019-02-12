class Node(object):
    """树的节点"""

    def __init__(self, item):
        self.elem = item
        self.left_child = None
        self.right_child = None


class Tree(object):
    """二叉树"""

    def __init__(self):
        self.root = None  # 根节点

    def add(self, item):  # 采用广度优先遍历法，放进队列中一层一层判断
        node = Node(item)  # 创建节点
        if self.root is None:  # 如果一开始，根节点就是空的，直接让新节点添加为根节点
            self.root = node
            return
        queue = [self.root]  # 先把根节点添加进去
        while queue:  # 只要队列不为空，就始终能拿出来节点进行判断
            cur_node = queue.pop(0)  # 当前的节点
            if cur_node.left_child is None:  # 判断当前节点的左子节点是否为空
                cur_node.left_child = node  # 为空就添加上新节点
                return
            else:
                queue.append(cur_node.left_child)  # 否则就把当前节点的左子节点放进队列待处理
            if cur_node.right_child is None:  # 判断当前节点的左子节点是否为空
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)
    