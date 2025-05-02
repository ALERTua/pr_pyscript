@service('pyscript.my_example_service')
def example_service(message='Default Message'):
    """example service using pyscript."""
    log.info("example_service executed")
    persistent_notification.create(
        notification_id="example_service",
        title="Example service notification title",
        message=message,
    )
