
# every monday at 10:00
# via https://crontab.guru/#0_10_*_*_1
@time_trigger("cron(0 10 * * 1)")
def monday_morning_trigger():
    log.info("Monday Morning. It's time to mow the lawn")
    vacuum.robot_mower.start()
