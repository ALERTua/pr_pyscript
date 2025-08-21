# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#state-trigger

@state_trigger("lock.door")
def door_lock_state_trigger():
    log.debug("Door Lock state changed!")

    light.hallway.toggle()
