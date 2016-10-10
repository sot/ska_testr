/usr/bin/git clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
git checkout master
py.test -v -s
