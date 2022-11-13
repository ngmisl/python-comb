import math

# player must select 2 skills
skills = ["Farming", "Melee", "Range", "Crafting", "Fishing", "Brewing"]


def main() -> None:
    num_skills: int = len(skills)
    variations: int = math.comb(num_skills, 2)
    print(variations)


if __name__ == "__main__":
    main()
