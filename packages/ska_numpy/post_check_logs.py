from testr.packages import check_files

# Compiler warnings can be skipped:
# http://stackoverflow.com/questions/25789055/
#   cython-numpy-warning-about-npy-no-deprecated-api-when-using-memoryview
# Circa Oct 2016, TLA tried upgrading cython (0.24) but this didn't help.

check_files('test_*.log', ['warning', 'error'],
            allows=['Using deprecated NumPy',
                    '_multiarray_api.h',
                    '__ufunc_api.h'])
