from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['1% quantile value of',
                    '1dpamzt violates planning limit',
                    '50% quantile value of',
                    '99% quantile value of',
                    '1dpamzt violates zero-feps limit',
                    'validation warning\(s\) in output',
                    'AstropyDeprecationWarning: out/states.dat already exists.',
                    'AstropyDeprecationWarning: headout/states.dat already exists.'])
