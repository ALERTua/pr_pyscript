
# Once every sunset
# via https://hacs-pyscript.readthedocs.io/en/stable/reference.html#time-trigger
@time_trigger("once(sunset)")
def sunset_trigger():
    log.info("The sun has set. Opening Windows")

    cover.kitchen_window.open_cover()

    cover.bedroom_window.open_cover()
