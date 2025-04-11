"""Dictionary Test"""

__author__: str = "730661635"

from exercises.ex03.dictionary import invert


def test_invert() -> None:
    """Test inversion of keys and values"""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_1() -> None:
    """Test inversion of keys and values"""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_edge() -> None:
    """Test inversion of keys and values"""
    assert invert({"a": "", "b": "c"}) == {"": "a", "c": "b"}


from exercises.ex03.dictionary import count


def test_count() -> None:
    """Test the count function"""
    assert count(["UNC", "Duke", "UNC"]) == {"UNC": 2, "Duke": 1}


def test_count_1() -> None:
    """Test the count function"""
    assert count(["UNC", "Duke", "UNC", "UNCG"]) == {"UNC": 2, "Duke": 1, "UNCG": 1}


def test_count_edge() -> None:
    """Test the count function"""
    assert count(["UNC", "Duke", "UNC", ""]) == {"UNC": 2, "Duke": 1, "": 1}


from exercises.ex03.dictionary import favorite_color


def test_favorite_color() -> None:
    """Test the favorite color function"""
    assert favorite_color({"Audra": "Blue", "Ashley": "Pink"}) == "Blue"


def test_favorite_color_1() -> None:
    """Test the favorite color function"""
    assert (
        favorite_color({"Audra": "Blue", "Ashley": "Pink", "Katie": "Pink"}) == "Pink"
    )


def test_favorite_color_edge() -> None:
    """Test the favorite color function"""
    assert favorite_color({}) == ""


from exercises.ex03.dictionary import bin_len


def test_bin_len() -> None:
    """Test the bin length function"""
    assert bin_len(["chapel", "hill", "dean", "dome"]) == {
        4: {"hill", "dean", "dome"},
        6: {"chapel"},
    }


def test_bin_len_1() -> None:
    """Test the bin length function"""
    assert bin_len(["dean", "dome"]) == {4: {"dean", "dome"}}


def test_bin_len_edge() -> None:
    """Test the bin length function"""
    assert bin_len(["", ""]) == {0: {""}}
