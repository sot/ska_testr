from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['99% quantile value of', 'in output at out'])
