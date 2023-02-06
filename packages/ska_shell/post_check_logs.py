from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=[r'test_[a-z]+_error'])
