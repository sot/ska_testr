# Get three launcher scripts manage.py update_events and update_cmds

GIT=`PATH=/usr/bin:$PATH which git`
$GIT clone ${TESTR_PACKAGES_REPO}/kadi
cp kadi/manage.py ./
rm -rf kadi

export KADI=$PWD
./manage.py makemigrations --no-input events
./manage.py migrate --no-input

START='2015:001'
STOP='2015:030'

kadi_update_events --start=$START --stop=$STOP
kadi_update_cmds --start=$START --stop=$STOP

# Write event and commands data using test database
./write_events_cmds.py --start=$START --stop=$STOP --data-root=events_cmds
