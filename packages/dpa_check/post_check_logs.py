from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['1% quantile value of',
                    '1dpamzt violates planning limit of 35.50 deg',
                    '50% quantile value of',
                    '99% quantile value of',
                    '1dpamzt violates zero-feps limit of 12.00 degC',
                    'validation warning\(s\) in output',
                    'AstropyDeprecationWarning: out/states.dat already exists.',
                    'AstropyDeprecationWarning: headout/states.dat already exists.'])
