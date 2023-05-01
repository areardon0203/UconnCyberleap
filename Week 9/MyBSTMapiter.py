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
        if not L:                                       #checks if list is empty
            return None                                 #returns none if it is
                                #sets node to root
        node = MyBSTNode(L[0])  
        while node is not None:
            print(node.key)
            left_list = [x for x in L[1:] if x < L[0]]      #Puts all nodes smalller than root in left list
            right_list = [x for x in L[1:] if x > L[0]]     #Puts all nodes larger than root in right list
            print(left_list)
            print(right_list)
        
        # node.left = MyBSTMap.frompreorder(left_list)    #Recursively calls left node
        # node.right = MyBSTMap.frompreorder(right_list)  #Recursively calls the right node
        # return node                                     #returns root node




    # @staticmethod

    # def frompostorder(L):
    #     if not L:
    #         return None
    #     node = MyBSTMap(L[-1])
    #     # print(node)
    #     left_list = [x for x in L[:-1] if x < L[-1]]
    #     right_list = [x for x in L[:-1] if x > L[-1]]
    #     node.left = MyBSTMap.frompostorder(left_list)
    #     node.right = MyBSTMap.frompostorder(right_list)
    #     return node
        

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTNode):
            return self.key == other.key and self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False
        

l = MyBSTMap()
x = [5,4,6,7]
for x in x:
    l.put(x, str(x))
# print(l)
# p = [(k,v) for (k,v) in l.preorder()]
# print(p)
lKey = [k for k in l.preorder()]
L2 = MyBSTMap.frompreorder(lKey)
print(L2)


