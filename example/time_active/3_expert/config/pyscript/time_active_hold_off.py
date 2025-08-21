from datetime import datetime

# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#time-active

# Trigger every minute minutes starting from the time of the HA startup
@time_trigger('period(now, 1min)')
# But only trigger if the cron expression matches
# from 0 to 15 minutes of hours 2 to 4 of every day.
# so it should be:
# - 02:00:00, 02:01:00, ... 02:15:00
# - 03:00:00, 03:01:00, ... 03:15:00
# - 04:00:00, 04:01:00, ... 04:15:00

# hold_off: "hold this trigger off for 119 seconds after triggering"
# it limits the trigger to only each second minute
# Yes, you could change the period, but his is only an example.
# so it should be:
# - 02:00:00, 02:02:00, ... 02:14:00
# - 03:00:00, 03:02:00, ... 03:14:00
# - 04:00:00, 04:02:00, ... 04:14:00
@time_active("cron(0-15 2-4 * * *)", hold_off=119)
def time_active_hold_off(trigger_time: datetime=None, trigger_type: str = None, **kwargs):
    log.info(f"Triggered by {trigger_type} at {trigger_time}")
