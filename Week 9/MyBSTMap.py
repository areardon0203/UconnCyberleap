from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if self.key is None and other.key is None:
            return True
        elif self.key == other.key:
            return True
        
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.

    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        if not L:
            return None
        node = MyBSTNode(L[0])
        left_list = [x for x in L[1:] if x < L[0]]
        right_list = [x for x in L[1:] if x > L[0]]
        node.left = MyBSTMap.frompreorder(left_list)
        node.right = MyBSTMap.frompreorder(right_list)
        return node

    @staticmethod
    def frompostorder(L):
        """ADD DOCSTRING"""

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTNode):
            return self.key == other.key and self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False
