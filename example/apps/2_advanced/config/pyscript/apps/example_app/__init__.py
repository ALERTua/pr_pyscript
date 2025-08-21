
# This service can be called using:
# - By executing a HA service in /developer-tools/action or anywhere else:
# ```yaml
#  action: pyscript.example_service
# ```
# - By calling `pyscript.example_service()` in pyscript code
@service
def example_service():
    """example service using pyscript."""
    log.info(f"example_service executed")
    light.toggle(entity_id='light.kitchen')
