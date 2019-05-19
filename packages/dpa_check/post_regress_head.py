import os
from testr.packages import make_regress_files

regress_files = ['headout/index.rst',
                 'headout/run.dat',
                 'headout/states.dat',
                 'headout/temperatures.dat']

clean = {'headout/index.rst': [(r'^Run time.*', '')],
         'headout/run.dat': [(r'#.*py run at.*', ''),
                         (os.environ['SKA'], '')]}

make_regress_files(regress_files, clean=clean)
