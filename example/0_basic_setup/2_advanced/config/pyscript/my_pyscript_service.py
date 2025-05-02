@service
def example_service():
    """example service using pyscript."""
    secret = pyscript.config["secrets"]["my_secret"]
    log.info(f"example_service executed. Secret: {secret}")
