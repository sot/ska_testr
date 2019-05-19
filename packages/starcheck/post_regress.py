from testr.packages import make_regress_files

regress_files = ['starcheck.txt',
                 'starcheck/pcad_att_check.txt']

clean = {'starcheck.txt': [(r'\s*Run on.*[\n\r]*', '')]}

make_regress_files(regress_files, clean=clean)
