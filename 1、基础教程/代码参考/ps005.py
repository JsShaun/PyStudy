


def decorator1(func):
    '''这里是装饰器1'''
    def wrapper(*args, **kwargs):
        print("当前执行函数或方法:{} ".format(func.__name__))
        print("当前函数参数:",*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorator1
def test(a,b,c):
    return a + b + c

d = test(1,2,3)
print(d)