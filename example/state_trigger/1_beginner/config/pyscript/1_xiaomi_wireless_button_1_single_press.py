# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#state-trigger

@state_trigger("sensor.xiaomi_wireless_button_1_action == 'single'")
def xiaomi_wireless_button_1_single_press():
    log.debug("xiaomi_wireless_button pressed once")
