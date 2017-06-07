import pytest
from domainCheck.value_result import ValueResult, TableValueResult


def test_validate_ValueResultObj():
    valueObj = ValueResult(14)
    assert valueObj.get_value() == {
        'type': 'ValueResult', 'value': 14}


def test_validate_wrong_input():
    with pytest.raises(ValueError):
        ValueResult({'1': 1})


def test_validate_TableValueResultObj():
    tableObj = TableValueResult([(1, 2, 3), (1, 2)])
    assert tableObj.get_value() == {
        'type': 'TableValueResult',
        'value': [(1, 2, 3), (1, 2)]
    }


def test_validate_list_of_non_tuples():
    with pytest.raises(ValueError):
        ValueResult([1, 2, 3])


def test_validate_dict():
    tableObjVar = TableValueResult({'1': 1, '2': 2})
    tableObj = tableObjVar.get_value()
    assert tableObj['type'] == 'TableValueResult'
    assert sorted(tableObj['value']) == [('1', 1), ('2', 2)]
