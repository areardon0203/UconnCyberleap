from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if self.root is None and other.root is None:
            return True
        elif self.root == other.root:
            return True
        elif self.root != other.root:
            return False 
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.

    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    
    def frompreorder(L):
        if not L:                                       #checks if list is empty
            return None                                 #returns none if it is
        node = MyBSTNode(L[0])                          #sets node to root
        left_list = [x for x in L[1:] if x < L[0]]      #Puts all nodes smalller than root in left list
        right_list = [x for x in L[1:] if x > L[0]]     #Puts all nodes larger than root in right list
        node.left = MyBSTMap.frompreorder(left_list)    #Recursively calls left node
        node.right = MyBSTMap.frompreorder(right_list)  #Recursively calls the right node
        return node                                     #returns root node

    @staticmethod
    def frompostorder(L):
        if not L:
            return None
        node = MyBSTNode(L[-1])
        left_list = [x for x in L[:-1] if x < L[-1]]
        right_list = [x for x in L[:-1] if x > L[-1]]
        node.left = MyBSTMap.frompostorder(left_list)
        node.right = MyBSTMap.frompostorder(right_list)
        return MyBSTMap(node)
        

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTNode):
            return self.key == other.key and self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False
