@time_trigger('period(now, 1h)')  # Trigger every hour starting from the time of the HA startup
@time_active('08:00:00', '22:00:00')  # Only trigger between 8am and 10pm
def hourly_trigger():
    log.info("Hourly trigger, but only between 8am and 10pm")
