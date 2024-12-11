import pytest


@pytest.fixture()
def setup():
    yield 12


print('test execution completed')


def test_sum_of_ele(setup):
    value = setup
    assert value == 12


def test_tsum_of_ele1(setup):
    value = setup
    assert value == 13, "required value should be 12"
