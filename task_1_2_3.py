class Node:
    """Клас вузла дерева з ключем та посиланнями на лівого, правого нащадка і висоту вузла (для AVL-дерева)."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Висота вузла, актуально для AVL-дерева


class BST:
    """Клас двійкового дерева пошуку (BST)."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Рекурсивне додавання нового ключа у двійкове дерево пошуку."""
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def find_max(self):
        """Пошук максимального елементу у двійковому дереві пошуку."""
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

    def find_min(self):
        """Пошук мінімального елементу у двійковому дереві пошуку."""
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def tree_sum(self):
        """Рекурсивно обчислює суму всіх значень у дереві."""
        return self._tree_sum(self.root)

    def _tree_sum(self, node):
        if node is None:
            return 0
        return node.key + self._tree_sum(node.left) + self._tree_sum(node.right)


class AVLTree(BST):
    """Клас AVL-дерева, яке є збалансованим двійковим деревом пошуку."""

    def _get_height(self, node):
        """Отримує висоту вузла. Повертає 0, якщо вузол порожній."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Обчислює баланс вузла (різниця висоти лівого та правого піддерева)."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, node):
        """Правий поворот навколо вузла z для балансування AVL-дерева."""
        y = node.left
        T3 = y.right
        y.right = node
        node.left = T3
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _left_rotate(self, node):
        """Лівий поворот навколо вузла z для балансування AVL-дерева."""
        y = node.right
        T2 = y.left
        y.left = node
        node.right = T2
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def insert(self, key):
        """Рекурсивне додавання нового ключа у AVL-дерево з підтримкою балансування."""
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # LL (лівий лівий) випадок
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        # RR (правий правий) випадок
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        # LR (лівий правий) випадок
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # RL (правий лівий) випадок
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node


if __name__ == "__main__":
    # Створюємо звичайне двійкове дерево пошуку
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(25)
    bst.insert(15)

    print("Максимальне значення у BST:", bst.find_max())
    print("Мінімальне значення у BST:", bst.find_min())
    print("Сума значень у BST:", bst.tree_sum())

    # Створюємо AVL дерево
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(25)
    avl.insert(15)

    print("Максимальне значення у AVL дереві:", avl.find_max())
    print("Мінімальне значення у AVL дереві:", avl.find_min())
    print("Сума значень у AVL дереві:", avl.tree_sum())
