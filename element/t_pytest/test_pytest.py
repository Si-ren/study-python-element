import pytest



class TestPytest:
    step = 0

    def setup_class(self):
        print('\n每个类的初始化操作')
        self.step = 18

    def setup_method(self):
        print('\n每个方法的前置操作')

    def teardown_class(self):
        print("\n每个类后销毁操作")

    def teardown_method(self):
        print("\n每个方法后执行操作")

    def test_setup_01(self, my_fixture):
        print('setup_01' + str(my_fixture))

    # 按顺序执行
    @pytest.mark.run(order=1)
    @pytest.mark.xxx
    def test_setup_02(self):
        print('setup_02')

    #   @pytest.mark.flaky(reruns=5, reruns_delay=2)
    @pytest.mark.skipif(step < 20, reason='小于步骤20')
    def test_setup_03(self):
        print(self.step)
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['--reruns 2'])
