from testr.packages import check_files

check_files(
    "test_*.log",
    ["warning", "error"],
    allows=[
        "WARNING.+because colnames",
        "WARNING.+made new file",
        "WARNING.+Unexpected null file",
        "test_logical_intervals_one_value_error PASSED",
        "test_state_intervals_one_value_error PASSED",
    ],
)
