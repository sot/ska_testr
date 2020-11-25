export ALLOW_NONSTANDARD_OFLSDIR=1

acisfp_check \
   --outdir=headout \
   --oflsdir=${SKA}/data/acis/LoadReviews/2018/MAY2818/oflsa \
   --nlet_file=${SKA}/data/acis/LoadReviews/NonLoadTrackedEvents.txt \
   --run-start=2018:142
