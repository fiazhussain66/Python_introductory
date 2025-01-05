cost_price = int(input("The cost price of the book: "))
selling_price = int(input("The selling price of the book: "))

if cost_price < selling_price:
    profit = selling_price - cost_price
    print("The profit of the book: ", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("The loss of the book", loss)
else:
    print("There is not any profit to sell book.")    
    
    
# Simple poker card rank check
# Define a card's rank and suit
rank = "Ace"
suit = "Hearts"

# Check card type using if-else
if rank == "Ace":
    print(f"The card is an {rank} of {suit}, typically considered high or low in value.")
elif rank == "King":
    print(f"The card is a {rank} of {suit}, one of the highest-ranking cards.")
elif rank == "Queen":
    print(f"The card is a {rank} of {suit}, a royal card.")
elif rank == "Jack":
    print(f"The card is a {rank} of {suit}, a face card.")
else:
    print(f"The card is a {rank} of {suit}, a numbered card.")
