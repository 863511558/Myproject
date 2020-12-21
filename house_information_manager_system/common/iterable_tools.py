"""
    可迭代对象工具集
"""


class IterableHelper:
    """
        可迭代对象助手
    """
# 静态方法:常用的工具,独立性强,不依赖于实例成员和类成员
    @staticmethod
    def find(iterable,func):
        number = 0
        for item in iterable:
            if func(item):
                number += 1
        return number
    @staticmethod
    def get_min(iterable,func):
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(min_value) > func(iterable[i]):
                min_value = iterable[i]
        return min_value
    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value
    @staticmethod
    def order_by(iterable,func):
        for i in range(len(iterable) - 1):
            for k in range(i + 1, len(iterable)):
                if func(iterable[i]) < func(iterable[k]):
                    iterable[i], iterable[k] = iterable[k], iterable[i]
    @staticmethod
    def order_down(iterable, func):
        for i in range(len(iterable) - 1):
            for k in range(i + 1, len(iterable)):
                if func(iterable[i]) > func(iterable[k]):
                    iterable[i], iterable[k] = iterable[k], iterable[i]
