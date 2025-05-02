@time_trigger("once(08:00:00)")  # 8AM every day
def morning_trigger():
    log.info("Good morning. Time to wake up! Opening Bedroom Window")
    cover.bedroom_window.open_cover()
