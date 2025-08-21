from random import choice

# every hour from sunset to one hour before sunrise
# via https://hacs-pyscript.readthedocs.io/en/stable/reference.html#time-trigger
@time_trigger('period(sunset, 1 hour, sunrise - 1 hour)')
def presence_simulation():
    entity_ids = [
        "light.living_room",
        "light.kitchen",
        "light.bedroom",
        "light.hallway",
    ]
    entity_id = choice(entity_ids)
    log.info(f"Toggling {entity_id} to simulate presence")
    homeassistant.turn_on(entity_id=entity_id)
    task.wait(10)  # wait 10 seconds between toggling lights
    homeassistant.turn_off(entity_id=entity_id)
