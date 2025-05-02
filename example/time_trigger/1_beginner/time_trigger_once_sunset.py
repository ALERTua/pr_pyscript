@time_trigger("once(sunset)")  # Once every sunset
def sunset_trigger():
    log.info("The sun has set. Opening Windows")
    cover.kitchen_window.open_cover()
    cover.office_window.open_cover()
    cover.bedroom_window.open_cover()
    cover.livingroom_window.open_cover()
