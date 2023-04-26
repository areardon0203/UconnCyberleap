from BSTNode import BSTNode

class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root:
            self.root = self.root.put(key,value)

        else:
            self.root = BSTNode(key, value)

    def get(self,key):
        if self.root:
            return self.root.get(key).value
        
        raise KeyError(f"key {key} is not in BSTMap")
    
    def __str__(self):
        if self.root:
            return self.root.print_subtree()
        
        else: return "Empty BST"

if __name__ == '__main__':
    bst = BSTMap()
    n = 4
    for i in range(4):
        print (f"putting{i}")
        bst.put(i,str(i))
        print(bst)
        