
# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#time-active
@time_trigger('period(now, 1h)')  # Trigger every hour starting from the time of the HA startup
@time_active("range(08:00, 22:00)")  # Only trigger between 8am and 10pm
def hourly_trigger():
    log.info("Hourly trigger, but only between 8am and 10pm")
