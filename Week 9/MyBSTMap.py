from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    def __eq__(self, other):
        """Check if two BSTs are equal"""
        if self.root is None and other.root is None:
            return True
    # If one root is None but the other isn't, they are not equal
        elif self.root is None or other.root is None:
            return False
    # If the keys and values of the roots are not equal, they are not equal
        elif self.root.key != other.root.key or self.root.value != other.root.value:
            return False
    # If both roots are equal, check if the left and right subtrees are equal recursively
        else:
            return self.root.left == other.root.left and self.root.right == other.root.right
    
    # TODO: implement the three methods below


    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod

    def frompreorder(L):
        if not L:
            return None
        # Create root node
        tree1 = MyBSTMap().newnode(L[0])
        stack = [tree1]
        for i in range(1,len(L)):          #adds the remaining nodes to list
            node = MyBSTMap().newnode(L[i])
            parent = None
            while stack and stack[-1].key < node.key:
                parent = stack.pop()
            
            if parent:
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)
        return stack                      #Returns the tree
    
    # def frompostorder(L):
    #     if not L:
    #         return None
    #     # Create root node
    #     tree1 = MyBSTMap()
    #     tree1.put(L[0])
    #     for i in range(1, len(L)):
    #         tree1.put(L[i])
    #     return tree1
        

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTNode):
            return self.key == other.key and self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False


if __name__ == "__main__":        
    bst1 = MyBSTMap()
    for k in [3, 1, 2]:                                #  Build the tree shown above
        bst1.put(k, str(k))
    print(bst1)
    L = [(k, v) for (k, v) in bst1.preorder()]         # construct preorder list
    bst2 = MyBSTMap.frompreorder(L)                    # reconstruct the original bst
    print(bst1 == bst2)