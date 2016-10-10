/usr/bin/git clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
git checkout master
py.test test.py -v -s
