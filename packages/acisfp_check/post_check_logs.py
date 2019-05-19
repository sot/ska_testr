from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['1% quantile value of',
                    '99% quantile value of',
                    'validation warning\(s\) in output',
                    'fptemp violates ACIS-I limit',
                    'fptemp violates FP-sensitive limit',
                    'AstropyDeprecationWarning: out/states.dat already exists.',
                    'AstropyDeprecationWarning: headout/states.dat already exists.'])
