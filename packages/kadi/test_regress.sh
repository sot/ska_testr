# Get three launcher scripts manage.py update_events and update_cmds

if [ ! -d "$SKA/data/mpcrit1/mplogs" ]
then
  echo "Directory $SKA/data/mpcrit1/mplogs not found, skipping regression test"
else
  export KADI=$PWD

  KADI_VERSION=`python -c 'import kadi; print(kadi.__version__)'`

  GIT=`PATH=/usr/bin:$PATH which git`
  $GIT clone ${TESTR_PACKAGES_REPO}/kadi

  cd kadi
  $GIT checkout $KADI_VERSION
  ./manage.py makemigrations --no-input events
  ./manage.py migrate --no-input
  cd ..
  rm -rf kadi

  # Note: the start time should be a day or two before the beginning of a
  # weekly load. This is need because the timeline_id for ORBPOINT events
  # uses the id of the first load segment in the week, so regression testing
  # will fail if the database creation starts midweek.
  START='2020:159:00:00:00'
  STOP='2020:189:00:00:00'

  kadi_update_events --start=$START --stop=$STOP
  kadi_update_cmds --start=$START --stop=$STOP

  # Write event and commands data using test database
  ./compare_values.py --start=$START --stop=$STOP --data-root=events_cmds
fi
