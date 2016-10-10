VERSION=`python -c "import kadi; print(kadi.__version__)"`
/usr/bin/git clone ${TESTR_PACKAGES_REPO}/${TESTR_PACKAGE}
cd ${TESTR_PACKAGE}
git checkout ${VERSION}
py.test kadi/tests -v -s
