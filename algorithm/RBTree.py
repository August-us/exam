class RBTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
    def find(self, key, node):
        if not node:
            return None
        elif key < node.data:
            return self.find(key, node.left)
        elif key > node.data:
            return self.find(key, node.right)
        else:
            return node
    def findMin(self, node):
        """
        找到以 node 节点为根节点的树的最小值节点 并返回
        :param node: 以该节点为根节点的树
        :return: 最小值节点
        """
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node
    def findMax(self, node):
        """
        找到以 node 节点为根节点的树的最大值节点 并返回
        :param node: 以该节点为根节点的树
        :return: 最大值节点
        """
        temp_node = node
        while temp_node.right:
            temp_node = temp_node.right
        return temp_node
    def transplant(self, tree, node_u, node_v):
        """
        用 v 替换 u
        :param tree: 树的根节点
        :param node_u: 将被替换的节点
        :param node_v: 替换后的节点
        :return: None
        """
        if not node_u.parent:
            tree.root = node_v
        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v
        elif node_u == node_u.parent.right:
            node_u.parent.right = node_v
        # 加一下为空的判断
        if node_v:
            node_v.parent = node_u.parent
    def left_rotate(self, node):
        '''
             * 左旋示意图：对节点x进行左旋
             *     parent               parent
             *    /                       /
             *   node                   right
             *  / \                     / \
             * ln  right   ----->     node  ry
             *    / \                 / \
             *   ly ry               ln ly
             * 左旋做了三件事：
             * 1. 将right的左子节点ly赋给node的右子节点,并将node赋给right左子节点ly的父节点(ly非空时)
             * 2. 将right的左子节点设为node，将node的父节点设为right
             * 3. 将node的父节点parent(非空时)赋给right的父节点，同时更新parent的子节点为right(左或右)
            :param node: 要左旋的节点
            :return:
        '''
        parent = node.parent
        right = node.right
        # 把右子子点的左子点节   赋给右节点 步骤1
        node.right = right.left
        if node.right:
            node.right.parent = node
        # 把 node 变成基右子节点的左子节点 步骤2
        right.left = node
        node.parent = right
        # 右子节点的你节点更并行为原来节点的父节点。 步骤3
        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right
    def right_rotate(self, node):
        '''
             * 左旋示意图：对节点y进行右旋
             *        parent           parent
             *       /                   /
             *      node                left
             *     /    \               / \
             *    left  ry   ----->   ln  node
             *   / \                     / \
             * ln  rn                   rn ry
             * 右旋做了三件事：
             * 1. 将left的右子节点rn赋给node的左子节点,并将node赋给rn右子节点的父节点(left右子节点非空时)
             * 2. 将left的右子节点设为node，将node的父节点设为left
             * 3. 将node的父节点parent(非空时)赋给left的父节点，同时更新parent的子节点为left(左或右)
            :param node:
            :return:
        '''
        parent = node.parent
        left = node.left
        # 处理步骤1
        node.left = left.right
        if node.left:
            node.left.parent = node
        # 处理步骤2
        left.right = node
        node.parent = left
        # 处理步骤3
        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
    def insert(self, node):
        # 找到最接近的节点
        temp_root = self.root
        temp_node = None
        while temp_root:
            temp_node = temp_root
            if node.data == temp_node.data:
                return False
            elif node.data > temp_node.data:
                temp_root = temp_root.right
            else:
                temp_root = temp_root.left
        # 在相应位置插入节点
        if not temp_node:
            # insert_case1
            self.root = node
            node.color = "BLACK"
        elif node.data < temp_node.data:
            temp_node.left = node
            node.parent = temp_node
        else:
            temp_node.right = node
            node.parent = temp_node
        # 调整树
        self.insert_fixup(node)
    def insert_fixup(self, node):
        if node.value == self.root.data:
            return
        # 为什么是这个终止条件？
        # 因为如果不是这个终止条件那就不需要调整
        while node.parent and node.parent.color == "RED":
            # 只要进入循环则必有祖父节点 否则父节点为根节点 根节点颜色为黑色 不会进入循环
            if node.parent == node.parent.parent.left:
                node_uncle = node.parent.parent.right
                # 1. 没有叔叔节点 若此节点为父节点的右子 则先左旋再右旋 否则直接右旋
                # 2. 有叔叔节点 叔叔节点颜色为黑色
                # 3. 有叔叔节点 叔叔节点颜色为红色 父节点颜色置黑 叔叔节点颜色置黑 祖父节点颜色置红 continue
                # 注: 1 2 情况可以合为一起讨论 父节点为祖父节点右子情况相同 只需要改指针指向即可
                if node_uncle and node_uncle.color == "RED":
                    # insert_case3
                    node.parent.color = "BLACK"
                    node_uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                    continue
                elif node == node.parent.right:
                    # insert_case4
                    self.left_rotate(node.parent)
                    node = node.left
                # insert_case5
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                self.right_rotate(node.parent.parent)
                return
            # 对称情况
            elif node.parent == node.parent.parent.right:
                node_uncle = node.parent.parent.left
                if node_uncle and node_uncle.color == "RED":
                    node.parent.color = "BLACK"
                    node_uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                    continue
                elif node == node.parent.left:
                    self.right_rotate(node)
                    node = node.right
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                self.left_rotate(node.parent.parent)
                return
        # 最后记得把根节点的颜色改为黑色 保证红黑树特性
        self.root.color = "BLACK"
    def delete(self, node):
        # 找到以该节点为根节点的右子树的最小节点
        node_color = node.color
        if not node.left:
            temp_node = node.right
            self.transplant(node, node.right)
        elif not node.right:
            temp_node = node.left
            self.transplant(node, node.left)
        else:
            # 最麻烦的一种情况 既有左子 又有右子 找到右子中最小的做替换 类似于二分查找树的删除
            node_min = self.findMin(node.right)
            node_color = node_min.color
            temp_node = node_min.right
            if node_min.parent != node:
                self.transplant(node_min, node_min.right)
                node_min.right = node.right
                node_min.right.p = node_min
            self.transplant(node, node_min)
            node_min.left = node.left
            node_min.left.parent = node_min
            node_min.color = node.color
        # 当删除的节点的颜色为黑色时 需要调整红黑树
        if node_color == "BLACK":
            self.delete_fixup(temp_node)
    def delete_fixup(self, node):
        # 实现过程还需要理解 比如为什么要删除 为什么是那几种情况
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                node_brother = node.parent.right
                if node_brother.color == "RED":
                    # delete_case2
                    node_brother.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right
                if (not node_brother.left or node_brother.left.color == "BLACK") and \
                        (not node_brother.right or node_brother.right.color == "BLACK"):
                    # delete_case3
                    node_brother.color = "RED"
                    node = node.parent
                else:
                    if not node_brother.right or node_brother.right.color == "BLACK":
                        # delete_case5
                        node_brother.color = "RED"
                        node_brother.left.color = "BLACK"
                        self.right_rotate(node_brother)
                        node_brother = node.parent.right
                    # delete_case6
                    node_brother.color = node.parent.color
                    node.parent.color = "BLACK"
                    node_brother.right.color = "BLACK"
                    self.left_rotate(node.parent)
                node = self.root
                break
            else:
                node_brother = node.parent.left
                if node_brother.color == "RED":
                    node_brother.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    node_brother = node.parent.right
                if (not node_brother.left or node_brother.left.color == "BLACK") and \
                        (not node_brother.right or node_brother.right.color == "BLACK"):
                    node_brother.color = "RED"
                    node = node.parent
                else:
                    if not node_brother.left or node_brother.left.color == "BLACK":
                        node_brother.color = "RED"
                        node_brother.right.color = "BLACK"
                        self.left_rotate(node_brother)
                        node_brother = node.parent.left
                    node_brother.color = node.parent.color
                    node.parent.color = "BLACK"
                    node_brother.left.color = "BLACK"
                    self.right_rotate(node.parent)
                node = self.root
                break
        node.color = "BLACK"
