#列表生成式
#List Comprehensions
# a = list(range(1,10))
# print(a)

# L = []
# for x in range(1,10):
#     L.append(x*x)

# print(L)  #结果[1, 4, 9, 16, 25, 36, 49, 64, 81]

# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2 == 0])  #取偶数

# print([m+n for m in 'ABC' for n in 'XYZ'])   #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# d = {'x':'A','y':'B','z':'C'}
# print([k + '=' + v for k,v in d.items()])   #['z=C', 'y=B', 'x=A']

L = ['Hello','World','Jackie']
print([s.lower() for s in L])
