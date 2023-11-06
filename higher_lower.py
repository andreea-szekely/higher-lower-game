import random
from higher_lower_art import logo, vs
from higher_lower_dataset import data

FOLLOWER_COUNT = "follower_count"
NAME = "name"
DESCRIPTION = "description"
COUNTRY = "country"

random.shuffle(data)

print(logo)

score = 0
left_comparison = 0
for right_comparison in range(1, len(data) - 1):
    left_item = data[left_comparison]
    print(
        f"Compare A: {left_item[NAME]}, a {left_item[DESCRIPTION]}, from {left_item[COUNTRY]}."
    )
    print(vs)
    right_item = data[right_comparison]
    print(
        f"Against B: {right_item[NAME]}, a {right_item[DESCRIPTION]}, from {right_item[COUNTRY]}."
    )
    selection = input("Who has more followers? Type 'A' or 'B'\n>").capitalize()
    left_item_count = left_item[FOLLOWER_COUNT]
    right_item_count = right_item[FOLLOWER_COUNT]
    if left_item_count > right_item_count:
        left_comparison = data.index(right_item)
        true_winner = data.index(left_item)
    else:
        left_comparison = data.index(left_item)
        true_winner = data.index(right_item)
    if (
        selection == "A"
        and left_item == data[true_winner]
        or selection == "B"
        and right_item == data[true_winner]
    ):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break
