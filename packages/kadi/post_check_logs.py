from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=[r'/kadi/settings.py:\d\d: UserWarning:',
                    r'warnings.warn\(message\)',
                    'Unable to change file mode',
                    'unable to get COBSRQID',
                    'alter_validators_add_error_messages',
                    'dropping state because of insufficent event time pad',
                    'negative event duration',
                    'Coarse OBC',
                    'no starcat for obsid 0'])
