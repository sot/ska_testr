from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['did not parse as fits unit',
                    'specified but multiple tables',
                    'has 2 aspect intervals'])
