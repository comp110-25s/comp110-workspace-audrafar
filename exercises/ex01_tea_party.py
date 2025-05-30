"Plan a tea party by calculating quantity of supplies and total cost."


__author__: str = "730661635"


def main_planner(guests: int) -> None:
    "Main function that puts all functions together"
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    "Compute the number of teabags based on number of guests."
    return people * 2


def treats(people: int) -> int:
    "Compute the number of treats based on number of teas."
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Compute the total cost of tea bags and treats."
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
