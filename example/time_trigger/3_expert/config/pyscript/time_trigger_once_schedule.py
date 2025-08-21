from datetime import datetime

TARGET_TEMP_ARG = "temperature"
TEMP_DEFAULT = 19
SHOWER_FLOOR_ENTITY_ID = "climate.shower_floor"

@time_trigger('once(08:00:00)', kwargs={TARGET_TEMP_ARG: 29})
@time_trigger('once(13:00:00)', kwargs={TARGET_TEMP_ARG: TEMP_DEFAULT})
@time_trigger('once(20:00:00)', kwargs={TARGET_TEMP_ARG: 27})
@time_trigger('once(21:30:00)', kwargs={TARGET_TEMP_ARG: 29})
@time_trigger('once(01:30:00)', kwargs={TARGET_TEMP_ARG: TEMP_DEFAULT})
# time_trigger provides `trigger_time` and `trigger_type`.
# kwargs from each time_trigger decorator fall into kwargs.
def shower_floor_temp(trigger_time: datetime=None, trigger_type: str = None, **kwargs):
    temperature_target = kwargs.get(TARGET_TEMP_ARG, TEMP_DEFAULT)
    log.info(f"{__name__} triggered by {trigger_type} at {trigger_time}:"
             f" setting shower floor target to {temperature_target}")
    climate.set_temperature(entity_id=SHOWER_FLOOR_ENTITY_ID, temperature=temperature_target)
