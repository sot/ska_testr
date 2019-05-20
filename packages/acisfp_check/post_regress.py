import os
from testr.packages import make_regress_files

regress_files = ['out/index.rst',
                 'out/run.dat',
                 'out/states.dat',
                 'out/temperatures.dat']

clean = {'out/index.rst': [(r'^Run time.*', ''),
                           ('Load directory.*', '')],
         'out/run.dat': [(r'#.*run at.*', ''),
                         (os.environ['SKA'], '')]}

make_regress_files(regress_files, clean=clean)
