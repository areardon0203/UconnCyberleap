class A(object):
    def dothis(self):
        print("doing this in A")
        a= 105
        print(a)

class B(A):
    print("Doing this in B")
    a= 10
    print(a)
    pass
    

class C(object):
    def dothis(self):
        print("doing this in C")
        a= 4
        print(a)


class D(C):
    pass

b_instance= B()

b_instance.dothis()

d_instance=D()

d_instance.dothis()