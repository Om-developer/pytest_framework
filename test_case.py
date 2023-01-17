import pytest

count_lst = ["hey this is hariom", 123, 345]


@pytest.mark.parametrize('test_count', count_lst)
@pytest.mark.parametrize('var', ['a', 'b', 'c'])
class Test_001:
    def test01(self, test_count, var):
        print(str(test_count), var)


""" this is for pytest parametrize and making pair of tests """
