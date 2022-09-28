from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['no starcat for obsid 0'])
