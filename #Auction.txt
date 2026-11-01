#Auction

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner=""
    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder


    print(f"Winner is {winner} with bidding amount {highest_bid}")

# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
auction_detail={}
# TODO-3: Whether if new bids need to be added
new_bid= True
while new_bid is True:
    name = input("What is your name?:".lower())
    price = int(input("What is your bid?: $".lower()))
    auction_detail[name]=price
    continue_bid=input("Are there any new bidder, type 'yes' or 'No':").lower()
    if continue_bid=="yes":
        print("\n" * 20)
    elif continue_bid=="no":
        new_bid=False
        find_highest_bidder(auction_detail)
