from abc import ABCMeta, abstractmethod


class BaseValueObj(metaclass=ABCMeta):
    value = None
    TYPE = None

    def __init__(self, value):
        self.value = self.validate(value)

    def get_value(self):
        return {'value': self.value, 'type': self.TYPE}

    @abstractmethod
    def validate(self, value):
        pass


class ValueObj(BaseValueObj):
    TYPE = 'value'

    def validate(self, value):
        if not isinstance(value, (int, float, str)):
            raise ValueError('Expected type: int, float, str')
        return value


class TableValueObj(BaseValueObj):
    TYPE = 'table'

    def validate(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, tuple):
                    raise ValueError('Expected tuple, got %i')
            return value
        elif isinstance(value, dict):
            return value.items()
        else:
            raise ValueError('Expected type: list, dict')


class ChartValueObj(TableValueObj):
    TYPE = 'chart'
