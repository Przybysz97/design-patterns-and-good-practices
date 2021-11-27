import timeit

class SAMPLE_PYLINT:

    def __init__(self, number):
        self._NUMBER = number

    def Divide(cls, number):
        if number == 0:
            raise ZeroDivisionError()


class children(SAMPLE_PYLINT):

    def __init__(self, name, PARAM, *args, **kwargs):
        self._name = name

    def some_method(self, param):
        if param == 1:
            return  True
        elif param == 2:
            return True
        elif param        ==3:
            return True
        elif param ==3:
            return True
        elif param ==3:
            return True
        else:
            return False

    def some_method2():
        print('bad implementation')


if __name__ == '__main__':
    sample = SAMPLE_PYLINT(10)
    try:
        sample.Divide(0)
    except Exception:
        pass
    sample.Divide()

    obj = children
    obj.some_method(4)

