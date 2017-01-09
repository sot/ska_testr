from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['test_inject_errors',
                    'test_inject_array_errors'])
