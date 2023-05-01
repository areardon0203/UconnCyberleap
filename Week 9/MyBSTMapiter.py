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
        
        node = MyBSTNode(L[0])

        left_list = [x for x in node.left if x is not None and x < node.value]
        right_list = [x for x in node.right if x is not None and x > node.value]

        yield node
    
        for child in frompreorder(left_list[1:]):
            yield child

        for child in frompreorder(right_list[1:]):
            yield child


    @staticmethod

    def frompreorder(L):
        if not L:
            return None
        
        node = MyBSTNode(L[0])

        left_list = [x for x in node.left if x is not None and x < node.value]
        right_list = [x for x in node.right if x is not None and x > node.value]
    
        for child in frompostorder(left_list[1:]):
            yield child

        for child in frompostorder(right_list[1:]):
            yield child

        yield node
        

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTNode):
            return self.key == other.key and self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False
        

# l = MyBSTMap()
# x = [5,4,6,7]
# for x in x:
#     l.put(x, str(x))
# print(l)
# p = [(k,v) for (k,v) in l.preorder()]
# print(p)

# L2 = list(MyBSTMap.frompreorder(p))
# print(L2)


