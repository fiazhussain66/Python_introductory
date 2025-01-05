import random

# Simulate rolling a dice
dice_roll = random.randint(1, 6)

# Draw a card from a deck
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_rank = random.choice(ranks)
card_suit = random.choice(suits)

print(f"You rolled a {dice_roll}")
print(f"You drew the {card_rank} of {card_suit}")

# Logical conditions
if dice_roll >= 5 and card_rank in ["Jack", "Queen", "King", "Ace"]:
    print("Wow! You hit a high card and a high roll!")
elif dice_roll <= 2 and card_rank in ["2", "3", "4", "5"]:
    print("Better luck next time; low roll and low card.")
elif dice_roll == 6:
    print("Perfect roll! Rolling the highest number is lucky!")
elif card_rank == "Ace":
    print("Lucky draw! The Ace is a strong card.")
else:
    print("Not bad! Try again for better luck.")
