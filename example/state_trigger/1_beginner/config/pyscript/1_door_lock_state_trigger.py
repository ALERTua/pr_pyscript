# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#state-trigger

@state_trigger("lock.door == 'unlocked'")  # trigger on door lock state changes to 'unlocked'
@time_active("range(18:00, 22:00)")  # but only between 6pm and 10pm
def door_unlocked_time_range():
    log.debug("Door Unlocked between 6pm and 10pm. Turning on the lights")
    light.hallway.turn_on()
