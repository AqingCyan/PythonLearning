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

    def breadth_travel(self):  # 遍历树
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self, node):  # 先序遍历每次根都在改变（一次次抽离不同的子树），所以我们传参
        """先序遍历"""
        if node is None:  # 最底层的子树决定了退出递归
            return
        print(node.elem, end=" ")  # 先序遍历，先打印当前的根节点，然后再处理左子树，再处理右子树
        self.preorder(node.left_child)  # 先左子树，以上一根节点的左子树为新的根节点
        self.preorder(node.right_child)

    def inorder(self, node):
        """中序遍历"""
        if node is None:  # 退出递归条件
            return
        self.inorder(node.left_child)  # 中序遍历，先打印左边节点，再打印当前树根节点，再打印右节点
        print(node.elem, end=" ")
        self.inorder(node.right_child)

    def postorder(self, node):
        """后序遍历"""
        if node is None:  # 退出递归条件
            return
        self.postorder(node.left_child)  # 后序遍历，先打印左边节点，再打印右节点，再打印当前树根节点
        self.postorder(node.right_child)
        print(node.elem, end=" ")


# 测试用例
tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.breadth_travel()  # 广度遍历
print()
tree.preorder(tree.root)  # 先序遍历
print()
tree.inorder(tree.root)  # 中序遍历
print()
tree.postorder(tree.root)  # 后序遍历
