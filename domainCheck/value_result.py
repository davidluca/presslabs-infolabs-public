from abc import ABCMeta, abstractmethod


class BaseValueResult(metaclass=ABCMeta):

    def __init__(self, value):
        self.value = self.validate(value)

    def get_value(self):
        return {'value': self.value, 'type': self.get_type()}

    def get_type(self):
        return self.__class__.__name__

    @abstractmethod
    def validate(self, value):
        pass


class ValueResult(BaseValueResult):

    def validate(self, value):
        if not isinstance(value, (int, float, str)):
            raise ValueError('Expected type: int, float, str')
        return value


class TableValueResult(BaseValueResult):

    def validate(self, value):
        if isinstance(value, list):
            for i in value:
                return self._validate_list(value)
        if isinstance(value, dict):
            return self._validate_dict(value)
        raise ValueError('Expected type: list, dict')

    def _validate_list(self, value):
        for values in value:
            if not isinstance(values, tuple):
                raise ValueError(
                    'Expected {} to pe a tuple, got {} insted'.format(
                        values, tyoe(value)))
        return value

    def _validate_dict(self, value):
        return list(value.items())


class ChartValueResult(TableValueResult):
    pass
