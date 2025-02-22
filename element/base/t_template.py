from string import Template

if __name__ == '__main__':
    t = Template("${name} is a ${token}")
    # substitute方法需要有几个变量传几个
    print(t.substitute(name="John", token="AKSHASHXZXCWA"))
    # safe_substitute方法可以少传 ， 未传的变量不会替换
    print(t.safe_substitute(name="John"))
    # 可以传字典
    print(t.safe_substitute({"name": "John", "token": "AKSHASHXZXCWA"}))

