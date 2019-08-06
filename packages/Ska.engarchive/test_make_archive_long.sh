# Test creating new engineering archive database and compare to flight data

mkdir data

CONTENTS="--content=acis2eng --content=acis3eng --content=acisdeahk --content=simcoor --content=orbitephem0"
START="2016:100"
STOP="2016:105"

export ENG_ARCHIVE=$PWD

# Create full resolution data
echo "Creating archive for normal full resolution MSIDs..."
cheta_update_server_archive --date-start $START --date-now $STOP --max-lookback-time=2 \
   --create --data-root=$PWD $CONTENTS

# Add derived parameter --content=dp_acispow128
#
echo "Creating dp_acispow128 archive files..."
export ENG_ARCHIVE=${PWD}:/proj/sot/ska/data/eng_archive
cheta_add_derived --start=$START --stop=$STOP --data-root=$PWD --content=dp_acispow
cheta_update_server_archive --date-start=$START --date-now=$STOP --data-root=$PWD --content=DP_ACISPOW --no-stats

# Add acispow derived parameters
CONTENTS="$CONTENTS --content=dp_acispow"

# Update stats.  --max-lookback-time is about 14 years.  Do not set so large
# that the start will be before 2000:001.
#
echo "Creating archive stats..."
cheta_update_server_archive --no-full --data-root=$PWD $CONTENTS --max-lookback-time=5000

# Compare newly created values to flight
echo "Comparing newly created values to flight"
./compare_values.py --start=$START --stop=$STOP $CONTENTS
