from testr.packages import check_files

check_files(
    'test_*.log', ['warning', 'error'],
    allows=[
        'using `oa_ndim == 0` when `op_axes` is NULL is deprecated.',
        'mica.archive.aca_dark.dark_model is deprecated.',
        'test_clip_warning PASSED',
    ]
)
