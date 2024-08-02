class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        trav = []
        def inorder_trav(start, res):
            if not start: return
            inorder_trav(start.left, res)
            res.append(start.value)
            inorder_trav(start.right, res)
        inorder_trav(self, trav)
        return trav