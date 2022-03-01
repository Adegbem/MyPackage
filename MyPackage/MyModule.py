def top_n(items, n):
    """
    return the top n item in an array, in a descending order
    :param items: array-like object or a list
    :param n: len of item to return
    :return: array, top n item in desecding order
    example:
            >>> top_n([8, 4, 2, 7, 9, 1], n=3)
            [9, 8, 7]
    """

    sorted_items = sorted(items, reverse=True)
    return sorted_items[:3]
