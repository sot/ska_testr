import glob

from testr.runner import make_regress_files

regress_files = glob.glob('events_cmds/*')
make_regress_files(regress_files)
