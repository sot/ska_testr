from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['WARNING.+because colnames',
                    'WARNING.+made new file',
                    'WARNING.+Unexpected null file',
                    'error.+one_value_error PASSED'])
