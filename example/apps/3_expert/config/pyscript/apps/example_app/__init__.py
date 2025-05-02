
registered_setup_example_app = {}

def setup_example_app(entity_id: str):

    task_name = f"{__name__}_{entity_id}"

    @state_trigger(entity_id, watch=[entity_id])
    def fnc_trigger(trigger_type=None, var_name=None, value=None, old_value=None, context=None, **kwargs):
        task.unique(task_name)
        log.info(f"{task_name}: {old_value}->{var_name}->{value}")

    registered_setup_example_app[task_name] = fnc_trigger



@time_trigger('once(now)')
def gen():
    for config in pyscript.app_config:
        setup_example_app(**config)
