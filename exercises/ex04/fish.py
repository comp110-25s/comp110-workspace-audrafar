"""File to define Fish class."""

__author__: str = "730661635"


class Fish:
    """Define fish class."""

    age: int

    def __init__(self):
        """Fish start at age 0."""
        self.age = 0
        return None

    def one_day(self):
        """Fish age by one each day."""
        self.age += 1
        return None
