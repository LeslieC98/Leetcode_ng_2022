class A:
    x = 0

    def func(self):
        print(self.x)


a = A()
a.x = 0

A.func(A)