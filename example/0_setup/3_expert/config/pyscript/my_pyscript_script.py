from tools import get_secret


@service
def example_service():
    """example service using pyscript."""
    secret = get_secret("my_secret")
    log.info(f"example_service executed. secret: {secret}")

    # services can be called via entity_id.action()
    cover.kitchen_window.open_cover()
    # or via domain.action(entity_id='entity_id')
    cover.open_cover(entity_id='cover.office_window')
    # or via service.call(domain, service, **kwargs)
    service.call("cover", "open_cover", entity_id="cover.bedroom_window")

    # this service can be called using
    # - pyscript.example_service()
    # - service.call("pyscript", "example_service")
