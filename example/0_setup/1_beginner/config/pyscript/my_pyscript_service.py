@service
def example_service():
    """example service using pyscript."""
    log.info("example_service executed")
    persistent_notification.create(
        notification_id="example_service",
        title="Example service notification title",
        message="Example service notification message",
    )
