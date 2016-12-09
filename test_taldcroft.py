import sys
from astropy.io.ascii import FastCsv
from astropy.io.ascii.cparser import CParserError
from hypothesis import given, settings
from hypothesis.strategies import text


@given(text(max_size=None))
@settings(max_examples=10000)
def test_it(s):
    print(repr(s))

    if sys.version_info[0] == 2:
        exceptions = CParserError, ValueError, IOError, TypeError
    else:
        exceptions = CParserError, ValueError, FileNotFoundError, IsADirectoryError

    try:
        FastCsv().read(s)
        print('Lucky guess!')
    except exceptions:
        # print('Invalid input')
        pass


if __name__ == '__main__':
    test_it()
