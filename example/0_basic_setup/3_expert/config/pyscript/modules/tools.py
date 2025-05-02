def get_secret(value):
    # noinspection PyUnresolvedReferences
    return pyscript.config.get('secrets', {}).get(value)
