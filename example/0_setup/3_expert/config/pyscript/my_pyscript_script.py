from tools import get_secret


@service
def example_service():
    """example service using pyscript."""
    secret = get_secret("my_secret")
    log.info(f"example_service executed. secret: {secret}")
