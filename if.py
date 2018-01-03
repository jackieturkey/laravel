# 利用if来实现python里面的 判断
# age = 20
# if age>= 18:
# 	print('真是好尴尬',age)
# 	print('成年了')
# else:
# 	print('还可以',age)
# 	print('没成年')
# try Anthoner once
# name = 18
# if name <= 12:
# 	print('MMP')
# elif name >= 18:
# 	print('woshinidaye')
# else:
# 	print('开心就好')

s = input('birth:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')
