def init():
    """Creates an instance of IndexHerbariorumApi class"""
    from indexherbariorum.client import IndexHerbariorumApi
    return IndexHerbariorumApi()


__all__ = ["init"]
