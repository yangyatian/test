class Test(object):
    def test1(self):
        print("这是一个测试！")
    def test2(self, num='abc'):
        for i in num:
            if i == 'a':
                print("这里包括a")
	def test3(self,a=1,b=2):
		c = a * b
		print(c)


if __name__ == "__main__":
    Test().test1()
    Test().test2()
	Test().test3()