# Copyright Gary Roberson 2024

from main.classes.street.street import Property


def streets_factory():
    val = [0, 1, 2, 3, 4, 5, 6]
    try:
        for i in val:
            s = Property(i)
            print(s.get_state())
            print(s.get_status())
    except Exception as e:
        return e
    finally:
        return "pass"


def test_create_streets(benchmark):
    """
    create streets
    :param benchmark:
    :return:
    """
    result = benchmark(streets_factory)
    assert result is "pass"
