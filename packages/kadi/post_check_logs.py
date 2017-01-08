from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
            allows=['/kadi/settings.py:\d\d: UserWarning:',
                    'warnings.warn\(message\)',
                    'Unable to change file mode',
                    'Coarse OBC'])
