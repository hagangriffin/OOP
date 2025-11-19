class Test:
    def __init__(self):
        self.var = 0

    def test(self):
        self.var += 1

    def printy(self):
        print(self.var)


s1 = Test()
s1.test()
s1.printy()
