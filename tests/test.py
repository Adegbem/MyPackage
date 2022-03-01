from MyPackage import MyModule


def test_top_n():
    """
    Making sure the function top_n works correctly
    :return: return a True or False case
    """
    assert MyModule.top_n([8, 36, 9, 3, 4], 2) == [36, 9], 'incorrect'
    assert MyModule.top_n([8, 10, 9, 3, 11, 23, 5], 5) == [23, 11, 10, 9, 8], 'incorrect'
    assert [36, 23, 11] == MyModule.top_n([8, 36, 9, 3, 4, 8, 10, 9, 3, 11, 23, 5], 3), 'incorrect'
