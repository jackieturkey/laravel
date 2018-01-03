#求1000以内的素数（质数）
#构造一个从三开始的奇数列
def _odd_iter():
    n = 1
    while True: 
        n = n+2
        yield n

#筛选函数
def _not_divisible(n):
    return lambda x: x%n >0
#生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
#给定条件，输出
for n in primes():
    if n < 10000:
        print(n)
    else:
        break
