def get_name(obj):
    """Get the name of an object."""
    return getattr(obj, '__name__', None)