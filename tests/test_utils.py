from src.utils import convert_1d_index_to_2d_index


def test_convert_1d_index_to_2d_index():
    x0, y0 = convert_1d_index_to_2d_index(0)
    assert x0 == 0
    assert y0 == 0

    y1, x1 = convert_1d_index_to_2d_index(1)
    assert x1 == 0
    assert y1 == 1

    y2, x2 = convert_1d_index_to_2d_index(2)
    assert x2 == 0
    assert y2 == 2

    y3, x3 = convert_1d_index_to_2d_index(3)
    assert x3 == 1
    assert y3 == 0

    y4, x4 = convert_1d_index_to_2d_index(4)
    assert x4 == 1
    assert y4 == 1

    y5, x5 = convert_1d_index_to_2d_index(5)
    assert x5 == 1
    assert y5 == 2

    y6, x6 = convert_1d_index_to_2d_index(6)
    assert x6 == 2
    assert y6 == 0

    y7, x7 = convert_1d_index_to_2d_index(7)
    assert x7 == 2
    assert y7 == 1

    y8, x8 = convert_1d_index_to_2d_index(8)
    assert x8 == 2
    assert y8 == 2
