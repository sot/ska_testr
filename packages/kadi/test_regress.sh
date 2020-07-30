# Get three launcher scripts manage.py update_events and update_cmds

if [ ! -d "$SKA/data/mpcrit1/mplogs" ]
then
  echo "Directory $SKA/data/mpcrit1/mplogs not found, skipping regression test"
else
  export KADI=$PWD

  GIT=`PATH=/usr/bin:$PATH which git`
  $GIT clone ${TESTR_PACKAGES_REPO}/kadi

  cd kadi
  ./manage.py makemigrations --no-input events
  ./manage.py migrate --no-input
  cd ..
  rm -rf kadi

  START='2015:001:12:00:00'
  STOP='2015:030:12:00:00'

  kadi_update_events --start=$START --stop=$STOP
  kadi_update_cmds --start=$START --stop=$STOP

  # Write event and commands data using test database
  ./compare_values.py --start=$START --stop=$STOP --data-root=events_cmds
fi
