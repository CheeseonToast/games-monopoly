# Copyright Gary Roberson 2024
"""
Taken from: https://refactoring.guru/design-patterns/singleton/python/example#example-1
To understand why a metdaclass check here: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

Using a mix between them both, which is thread safe and also work with Python 2 and 3

============
Usage for Python 2 and 3 at the same time
============
---
Class Definition
---

Define the class like this
class Logger(Singleton):
    pass

---
Usage
---
Then use like this
def test_singleton(value: str) -> None:
    logger = Logger(value)
    print(logger.value)
"""
from config.porting import Porting

if Porting.is_python_3_or_newer():
    from threading import Lock


class _Singleton(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    if Porting.is_python_3_or_newer():
        _lock = Lock()

    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if Porting.is_python_3_or_newer():
            # Now, imagine that the program has just been launched. Since there's no
            # Singleton instance yet, multiple threads can simultaneously pass the
            # previous conditional and reach this point almost at the same time. The
            # first of them will acquire lock and will proceed further, while the
            # rest will wait here.
            with cls._lock:
                # The first thread to acquire the lock, reaches this conditional,
                # goes inside and creates the Singleton instance. Once it leaves the
                # lock block, a thread that might have been waiting for the lock
                # release may then enter this section. But since the Singleton field
                # is already initialized, the thread won't create a new object.
                if cls not in cls._instances:
                    # Changing how we access to read from 7
                    cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            if cls not in cls._instances:
                cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


# works in Python 2 & 3
class Singleton(_Singleton('SingletonMeta', (object,), {})):
    pass