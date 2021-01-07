import os
from pathlib import Path
import getpass
from testr.packages import check_files


allows = ['did not parse as fits unit',
          'specified but multiple tables',
          'has 2 aspect intervals',
          'NaturalNameWarning:']

# If the running user does not have a Sybase V&V access file, ignore report test fail.
user = getpass.getuser()
auth_file = Path(os.environ['SKA']) / 'data' / 'aspect_authorization' / f'sqlsao-axafvv-{user}'
if not auth_file.exists():
    allows.append('UserWarning: On HEAD but no sybase access.')

check_files('test_*.log', ['warning', 'error'],
            allows=allows)
