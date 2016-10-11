import glob

from testr.packages import make_regress_files

regress_files = glob.glob('events_cmds/*')
make_regress_files(regress_files)
