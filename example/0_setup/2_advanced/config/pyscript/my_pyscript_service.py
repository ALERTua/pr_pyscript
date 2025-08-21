@service
def example_service():
    """example service using pyscript."""
    secret = pyscript.config["secrets"]["my_secret"]
    log.info(f"example_service executed. Secret: {secret}")

    # services can be called via entity_id.action()
    cover.kitchen_window.open_cover()
    # or via domain.action(entity_id='entity_id')
    cover.open_cover(entity_id='cover.office_window')
    service.call("cover", "open_cover", entity_id="cover.bedroom_window")

    # all `/developer-tools/action` can be called this way.
    homeassistant.turn_on(entity_id='light.office')

    # this service is registered as an action among other actions and can be called using
    # - Code call `pyscript.example_service()`
    # `/developer-tools/action` action:
    # ```yaml
    # action: pyscript.example_service
    # ```
