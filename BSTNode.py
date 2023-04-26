# class Tree:
#     def __init__(self, L):
#         iterator = iter(L)
#         self.data = next(iterator)
#         self.children = [Tree(c) for c in iterator]

#     def __eq__(self, other):
#         return self.data == other.data and self.children == other.children

#     def _listwithlevels(self, level, trees):
#         trees.append(" " * level + str(self.data))
#         for child in self.children:
#             child._listwithlevels(level + 2, trees)

#     def __str__(self):
#         trees = []
#         self._listwithlevels(0, trees)
#         return "\n".join(trees)
    

# T = Tree(["a", ["b", ["c", ["d"]]],["e",["f"], ["g"],["h",["p"],["q",[1]]]]])
                                                
# print(str(T))

# Binary Node Class
class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None #left child
        self.right = None #right child
        self.weight = 1 #number of nodes in subtree rooted at this node

    #update value or add key:value pair
    def put(self,key,value):
        if self.key == key:
            self.value = value

        elif self.key > key: #search left
            if self.left: self.left.put(key, value)
            else: self.left = BSTNode(key, value)

        elif self.key < key: #search right
            if self.right: self.right.put(key, value)
            else: self.right = BSTNode(key,value)
        
        update_weight(self)

        def update_weight(self):
            left_weight = self.left.weight if self.left else 0
            right_weight = self.right.weight if self.right else 0
            self.weight = left_weight + right_weight + 1

    #return node with matching key
    def get(self,key):
        #3 cases
            #1) self.key == key: return self
            #2) self.key > key: search left
            #3) self.key < key: search right
    
        if self.key == key: return self

        if self.key > key:
            if self.left: return self.left.get(key)
        
        if self.key < key:
            if self.right: return self.right.get(key)
        
        raise KeyError(f"key {key} is not in tree")
    
    # return the node with matching key or next closest (lowest key)
    def floor(self, key):
        # 3 cases:
        if self.key == key: return self
 
        #self.key > key: search left subtree
        #return left.floor or return None
        if self.key > key:
            if self.left: return self.left.floor(key)
            else: return None

        if self.key < key:
            if self.right:
                temp_node = self.right.floor(key)
                if temp_node: return temp_node        
                else: return self
            
            else: return self
