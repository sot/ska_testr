GIT=`PATH=/usr/bin:$PATH which git`
$GIT clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
$GIT checkout master
py.test -v -s
