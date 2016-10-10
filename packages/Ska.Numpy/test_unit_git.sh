/usr/bin/git clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
git checkout master
python setup.py build_ext --inplace
py.test test.py -v -s
