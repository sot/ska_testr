import xija
n_fail = xija.test('-v', '-s', '-k not test_minusz')
if n_fail > 0:
    raise ValueError(str(n_fail) + ' test failures')
