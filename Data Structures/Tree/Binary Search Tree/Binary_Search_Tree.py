class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(cur):
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return True
                else:
                    return _insert(cur.left)
            elif value > cur.value:
                if cur.right is None:
                    cur.right = Node(value)
                    return True
                else:
                    return _insert(cur.right)
            else:  # value == cur.value
                print(f"{value} is already exist in the tree")
                return False

        if self.root is None:
            self.root = Node(value)
            return True

        return _insert(self.root)

    def search(self, target):
        cur = self.root

        while cur:
            if target < cur.value:
                cur = cur.left
            elif target > cur.value:
                cur = cur.right
            else:  # target == cur.value
                return True
        # Not found
        return False

    def delete(self, target):
        cur = parent = self.root

        while cur:
            if target < cur.value:
                parent = cur
                cur = cur.left
            elif target > cur.value:
                parent = cur
                cur = cur.right
            else:  # target == cur.value
                break
        else:  # Not found
            print(f"{target} is not exist in the tree")
            return False

        # target node has no child
        if cur.left is None and cur.right is None:
            if cur == self.root:
                self.root = None
                return True
            elif target < parent.value:
                parent.left = None
            else:
                parent.right = None
        # target node has only left child
        elif cur.left and cur.right is None:
            if cur == self.root:
                self.root = self.root.left
                return True
            elif target < parent.value:
                parent.left = cur.left
            else:
                parent.right = cur.left
        # target node has only right child
        elif cur.left is None and cur.right:
            if cur == self.root:
                self.root = self.root.right
                return True
            elif target < parent.value:
                parent.left = cur.right
            else:
                parent.right = cur.right
        else:  # target node has both child
            successor = successor_parent = cur.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            cur.value = successor.value
            if successor.right is None:
                if cur.right == successor:
                    cur.right = None
                else:
                    successor_parent.left = None
            else:  # Successor has right child
                if cur.right == successor:
                    cur.right = successor.right
                else:
                    successor_parent.left = successor.right
        return True

    def preorder(self):
        pre_list = []

        def _preorder(cur):
            if cur is None:
                return
            pre_list.append(cur.value)
            _preorder(cur.left)
            _preorder(cur.right)

        _preorder(self.root)
        print("Preorder ->", pre_list)

    def inorder(self):
        in_list = []

        def _inorder(cur):
            if cur is None:
                return
            _inorder(cur.left)
            in_list.append(cur.value)
            _inorder(cur.right)

        _inorder(self.root)
        print("Inorder ->", in_list)

    def postorder(self):
        post_list = []

        def _postorder(cur):
            if cur is None:
                return
            _postorder(cur.left)
            _postorder(cur.right)
            post_list.append(cur.value)

        _postorder(self.root)
        print("Postorder ->", post_list)


if __name__ == "__main__":
    #               50
    #            /     \
    #          27       66
    #        /   \    /   \
    #      15    30  58   70
    #     /  \    \    \
    #    7   20   41   61

    my_bst = BST()
    my_bst.insert(50)
    my_bst.insert(27)
    my_bst.insert(15)
    my_bst.insert(30)
    my_bst.insert(66)
    my_bst.insert(58)
    my_bst.insert(70)
    my_bst.insert(61)
    my_bst.insert(7)
    my_bst.insert(20)
    my_bst.insert(41)
    my_bst.insert(41)
    my_bst.preorder()
    my_bst.inorder()
    my_bst.postorder()
    print(my_bst.search(15))
    print(my_bst.search(219))
    my_bst.delete(1)
    my_bst.delete(27)
    my_bst.delete(7)
    my_bst.delete(58)
    my_bst.delete(50)
    my_bst.preorder()
    my_bst.inorder()
    my_bst.postorder()

# 41 is already exist in the tree
# Preorder -> [50, 27, 15, 7, 20, 30, 41, 66, 58, 61, 70]
# Inorder -> [7, 15, 20, 27, 30, 41, 50, 58, 61, 66, 70]
# Postorder -> [7, 20, 15, 41, 30, 27, 61, 58, 70, 66, 50]
# True
# False
# 1 is not exist in the tree
# Preorder -> [61, 30, 15, 20, 41, 66, 70]
# Inorder -> [15, 20, 30, 41, 61, 66, 70]
# Postorder -> [20, 15, 41, 30, 70, 66, 61]