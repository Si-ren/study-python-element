#如果闭包函数的参数有且只有一个并且是函数类型，那么这个闭包函数称为装饰器
import time


def work_time(func):
    def inner(num):
        start_time = time.time()
        func(num)
        end_time = time.time()
        print(end_time - start_time)
    return inner

@work_time
def work(num):
    time.sleep(num)

if __name__ == '__main__':
    work(3)
