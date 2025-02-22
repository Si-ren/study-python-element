```text
pytest
pytest-html   #生成html格式的自动化测试报告
pytest-xdist    #测试用例分布式执行.多CPU分发
pytest-ordering #用于改变测试用例执行顺序
pytest-rerunfailures    #用例失败后重跑,https://github.com/pytest-dev/pytest-rerunfailures
allure-pytest   #用于生成美观的测试报告
```
### pytest默认规则
```text
1.模块名必须以test 开头或者 test结尾
2.测试类必须以Test开头，并且不能有init方法。
3.测试方法必须以test开头
```
### pytest测试用例运行方式
```text
1.主函数模式
    1. 运行所有：pytest.main()
    2. 指定模块：pytest.main(['-vs','xxxx.py'])
    3. 指定目录：pytest.main(['-vs','./xxxx_dir'])
    4. 指定nodeID: pytest.main(['-vs','./xxxx_dir/xxx.py::TestInterface::test_function'])
2.命令行模式
    1. 运行所有：pytest
    2. 重试失败的用例2次：pytest -vs .\test_pytest.py --reruns 5 
3.通过读取pytest.ini配置文件运行
    pytest.ini 文件是 pytest 单元测试框架的核心配置文件。
    位置：一般放在项目的根目录下
    编码：必须是ANSI，可以使用noepad++修改编码
    作用：改变 pytest 默认的行为(可以更改模块名以test等等规定)
    运行的规则：不管是主函数的模式运行，还是命令行模式运行，都会去读取这个配置文件。
```
```ini
[pytest]
addopts = -p no:warnings -vs 
testpaths = ./testcase
python_files = test_*.py
python_classes = Test*
python_functions = test*
```

| 参数	                         | 说明及使用                                         |
|-----------------------------|-----------------------------------------------| 
| -s	                         | 表示输出调试信息，包括print打印信息                          |
| -v	                         | 表示更详细的信息，通常-vs一起使用                            |
| -n	                         | 支持多线程或者分布式运行测试用例 pytest -vs ./testcase01 -n 2 |
| -m	                         | 分组执行                                          |
| --reruns <num>              | 失败用例重新运行                                      | 
| -x                          | 失败一个用例就停止                                     |
| --maxfail <num>             | 失败num个用例停止                                    |
| -k                          | 根据字符串筛选用例 -k "ao"                             |
| --html ./report/repost.html | 生成html测试报告                                    |
|                             |                                               |


### 执行顺序
默认从上到下
使用  @pytest.mark.run(order=1)  修改执行顺序

### 分组执行
```python
@pytest.mark.<分组名称>
```
```ini
pytest.ini:
    markers=
        xxx: 测试分组
```
```shell
pytest.exe -m 'aaa or bbb'
```

### 跳过用例
@pytest.mark.skip(reason='小于步骤20')
@pytest.mark.skipif(step < 20, reason='小于步骤20')

### setup_class/teardown_class  setup_method/teardown_method
```python
    def setup_class(self):
        print('\n每个类的初始化操作')
        self.step = 18

    def setup_method(self):
        print('\n每个方法的前置操作')

    def teardown_class(self):
        print("\n每个类后销毁操作")

    def teardown_method(self):
        print("\n每个方法后执行操作")
```

### @pytest.fixture用法 比setup/teardown更灵活
1. scope: 用于控制Fixture的作用范围
默认取值为function（函数级别），控制范围的排序为：session > module > class > function

| 取值 | 范围说明 |
|-----|---------| 
|  function | 函数级 每一个函数或方法都会调用 |
| class   | 函数级 模块级 每一个.py文件调用一次     |
| module   |  模块级 每一个.py文件调用一次    |
| session   |  会话级 每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法    |

2. params: Fixture的可选形参列表，支持列表传入
默认None，每个param的值
fixture都会去调用执行一次，类似for循环
可与参数ids一起使用，作为每个参数的标识，详见ids
被fixture装饰的函数要调用是采用：request.param
3. ids: 用例标识ID ,与params配合使用，一对一关系
4. autouse: 默认False
若为True，刚每个测试函数都会自动调用该fixture,无需传入fixture函数名
由此我们可以总结出调用fixture的三种方式：
    1. 函数或类里面方法直接传fixture的函数参数名称
    2. 使用装饰器@pytest.mark.usefixtures()修饰
    3. autouse=True自动调用，无需传仍何参数，作用范围跟着scope走（谨慎使用）
5. name: fixture的重命名
如果使用了name,那只能将name传入，函数名不再生效

### conftest.py文件是pytest一个组件，可以实现全局的配置
1. 单独存放fixture的一个配置文件，可以在每个目录下有一个
2. 可以在当前目录下所有的py文件使用
3. 原则上conftest.py和运行的用例放到同一层，不需要任何import导入操作