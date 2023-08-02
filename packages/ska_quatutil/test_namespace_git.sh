GIT=`PATH=/usr/bin:$PATH which git`
$GIT clone ${TESTR_PACKAGES_REPO}/Ska.quatutil
cd Ska.quatutil
$GIT checkout master
py.test -v -s
