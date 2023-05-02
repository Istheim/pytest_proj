from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([], 0, None) is None
    assert arrs.get([100, 200, 300], -1) == 300
    assert arrs.get([], 2, None) is None
    assert arrs.get([10, 20, 30], 4, None) is None
    assert arrs.get([15, 25, 35], -10, None) is None
    assert arrs.get([], -3, None) is None
    assert arrs.get([2, 3, 4], -2) == 3


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-2) == [4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-5, end=-1) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -10) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 2) == []
    assert arrs.my_slice([], 0, 0) == []


