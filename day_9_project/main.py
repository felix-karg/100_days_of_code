# Blind auction

from art import logo

print(logo)

bids = {}
new_bid = True

while new_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    another_bid = input("Are there any other bidders? Type 'yes' or 'no' ")

    if another_bid == "no":
        new_bid = False

    bids[name] = bid

highest_bid = 0
highest_bidder = ""
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
