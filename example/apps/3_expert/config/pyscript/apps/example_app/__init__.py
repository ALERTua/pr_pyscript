# 4
# so why do we make a factory just to make a few state triggers?
# because by using this factory we can generate such trigger for one more config
# just by adding a few lines in config.yaml instead of copy-pasting the whole state_trigger-wrapped function
registered_setup_example_app = {}

# 3
# this is where an application receives its arguments
# notice we expect entity_id to exist, otherwise this setup will fail
# notice we assume other arguments can be passed, and we can process them using kwargs
def setup_example_app(entity_id: str, **kwargs):

    # notice we use entity_id here
    task_name = f"{__name__}_{entity_id}"

    # notice passing other_kwarg is optional
    my_variable = kwargs.get('other_kwarg', 'default_value')

    @state_trigger(entity_id, watch=[entity_id])
    def fnc_trigger(trigger_type=None, var_name=None, value=None, old_value=None, context=None, **kwargs):
        task.unique(task_name)
        log.info(f"{task_name}: {old_value}->{var_name}->{value}")
        log.info(f"by the way, {my_variable=}")

    registered_setup_example_app[task_name] = fnc_trigger



@time_trigger('once(now)')  # parse the config once every startup or after this file or config change
def gen():
    # 1
    # for each entry in an array in the pyscript config.yaml for this particular application
    # E.g.
    # ```yaml
    # apps:
    # # you must parse it according to its type. in this example we are working with dictionaries
    #   example_app:
    #     - entity_id: sun.sun
    #     - entity_id: update.hacs_update
    # ```
    # for each of these configs, set up an example_app application
    for config in pyscript.app_config:
        # 2
        # notice here we treat each config as a dictionary (we pass **config to the setup_example_app)
        # so the proper list of configurations for this application would be:
        # ```yaml
        #   example_app:
        #     - entity_id: sun.sun  # this is a dictionary
        #       other_kwarg: some value
        #     - entity_id: update.hacs_update  # this is also a dictionary
        # ```
        setup_example_app(**config)
