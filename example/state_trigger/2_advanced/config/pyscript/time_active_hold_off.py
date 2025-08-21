# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#time-active

# Trigger every minute starting from the time of the HA startup
@time_trigger('period(now, 1min)')
# But only trigger between 8am and 10pm
# And only once every 2 minutes (hold_off)
# Yes, this is stupid, but it is only an example.
# "hold this trigger off for 120 seconds after triggering"
@time_active("range(08:00:00, 22:00:00)", hold_off=120)
def time_active_hold_off():
    log.info("Trigger, but only between 8am and 10pm")
