"""Program that calculates the cost of a teaparty based on
 the number of people and drinks/food"""

__author__: str = "730771568"


def main_planner(guests: int):
    """Calculates items needed for teaparty of n guests and the cost"""
    tea = tea_bags(guests)
    treat = treats(guests)
    costs = cost(tea, treat)
    print("Tea Bags: ", tea)
    print("Treats: ", treat)
    print("Cost: $", costs)


def tea_bags(people: int) -> int:
    """Calculates the number of teabags needed based on the number of people"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates the number of treats needed based on the number of people"""
    tea = tea_bags(people=people)
    treats = 1.5 * tea
    return int(treats)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost of the tea party"""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
