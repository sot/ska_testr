from testr.packages import check_files

check_files('test_*.log', ['warning', 'error'],
    allows=[
        "WARNING.+compare_common_columns keys",
    ])
