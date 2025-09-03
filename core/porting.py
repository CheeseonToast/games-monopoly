# Copyright Gary Roberson 2024
import sys


class Porting(object):

    @staticmethod
    def is_python_3_or_newer():
        return sys.version_info[0] > 2
