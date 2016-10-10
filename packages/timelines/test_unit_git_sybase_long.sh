# Command states scripts and module already installed in skadev
/usr/bin/git clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
git checkout master
# nosetests timelines_test.py
