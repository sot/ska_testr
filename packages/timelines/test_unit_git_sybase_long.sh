# Command states scripts and module already installed in skadev
GIT=`PATH=/usr/bin:$PATH which git`
$GIT clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
$GIT checkout master
# nosetests timelines_test.py
