"""File to define Bear class."""

__author__: str = "730661635"


class Bear:
    """Define bear class"""

    age: int
    hunger_score: int

    def __init__(self):
        """Bears start at age 0 and hunger score 0"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Bears age by 1 each day and lose one hunger score"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Hunger score goes up as bears eat fish"""
        self.hunger_score = self.hunger_score + num_fish
