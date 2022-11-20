from replit import clear
should_continue  = True
bidding_directory = {}
while should_continue:
    name =  input("What is your name?")
    bid_amount = int(input("What is your bid? $"))
    bidding_directory[name] = bid_amount

    bidders_left = input("Are there any other bidders? yes or no?  ").lower()
    clear()
    if bidders_left == "no":
        should_continue = False
    elif bidders_left == "yes" :
        should_continue = True
    else:
        print("Wrong input, Please type 'yes' or 'no'")






winner = ""
winning_bid = 0

for bidder in bidding_directory:
    bid = bidding_directory[bidder]
    if bidding_directory[bidder] > winning_bid:
        winning_bid =  bid
        winner = bidder

print(f"The winner is {winner} with a bid of {winning_bid}. ")





        


