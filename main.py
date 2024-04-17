total_money = 5000 # total money in pocket willing to spend at roulette table
min_bet = 10 # minimum bet limit

def halfs(bet, max):
    # Function for halfs (odd, even) (red, black) (1-18 , 19-36)
    print(" ")
    print("Calculations for HALFS")
    print(" ")
    losses = 0
    round = 1
    one_zero = (37 - 18) / 37 # odds of losing per play with one 0
    two_zeros = (38 - 18) / 38 # odds of losing per play with double 0
    lose_chance_0 = one_zero # variable to be used to calculate total chance to lose every round with one 0
    lose_chance_00 = two_zeros # variable to be used to calculate total chance to lose every round with double 0
    while bet + losses <= max: # loop until I cannot afford to bet anymore
        print(f"---------- Round {round} ----------")
        print(f"Bet: {bet}")
        print(f"Chance to lose with 0: {lose_chance_0 * 100}%") # chance to lose in total this round with one 0
        print(f"Chance to lose with 00: {lose_chance_00 * 100}%") # chance to lose in total this round with double 0        
        print(f"Total winnings: {bet * 2}") # calculation of total money won if I win this round
        losses += bet # Calculation of total money spent so far
        print(f"Total spent: {losses}") # printing the total money spent so far
        print(f"You would win: {bet * 2 - losses}") # How much money I have left over from winning - losses so far
        print(f"Total money left: {max - losses}") # How much money I have left to bet with in my pocket
        bet *= 2 # calculating next bet cost
        bet = int(bet + 0.5) # rounding up to closest whole number (integer)
        lose_chance_0 *= one_zero # calculating chance to lose for next round with one 0
        lose_chance_00 *= two_zeros # calculating chance to lose for next round with double 00
        round += 1 # iterating the round number

def thirds(bet, max):
    # Function for thirds (columns 1, 2, 3) (dozens 1-12, 13-24, 25-36)
    print(" ")
    print("Calculations for THIRDS")
    print(" ")    
    losses = 0
    round = 1
    one_zero = (37 - 12) / 37 # odds of losing per play with one 0
    two_zeros = (38 - 12) / 38 # odds of losing per play with double 0
    lose_chance_0 = one_zero # variable to be used to calculate total chance to lose every round with one 0
    lose_chance_00 = two_zeros # variable to be used to calculate total chance to lose every round with double 0
    while bet + losses <= max: # loop until I cannot afford to bet anymore
        print(f"---------- Round {round} ----------")
        print(f"Bet: {bet}")
        print(f"Chance to lose with 0: {lose_chance_0 * 100}%") # chance to lose in total this round with one 0
        print(f"Chance to lose with 00: {lose_chance_00 * 100}%") # chance to lose in total this round with double 0        
        print(f"Total winnings: {bet * 3}") # calculation of total money won if I win this round
        losses += (bet) # Calculation of total money spent so far
        print(f"Total spent: {losses}") # printing the total money spent so far
        print(f"You would win: {bet * 3 - losses}") # How much money I have left over from winning - losses so far
        print(f"Total money left: {max - losses}")  # How much money I have left to bet with in my pocket
        bet *= 1.5  # calculating next bet cost
        bet = int(bet + 0.5) # rounding up to closest whole number (integer)
        lose_chance_0 *= one_zero # calculating chance to lose for next round with one 0
        lose_chance_00 *= two_zeros # calculating chance to lose for next round with double 00
        round += 1 # iterating the round number


halfs(min_bet, total_money)
thirds(min_bet, total_money)

print("----------HALFS----------")
# same as above function for halfs but only shows the bets per round
bet_calc = min_bet
spent = min_bet
while bet_calc <= total_money:
    print(f"{bet_calc}")
    bet_calc *= 2
    bet_calc = int(bet_calc + 0.5)
    spent += bet_calc

print("----------THIRDS----------")
# same as above function for thirds but only shows the bets per round
bet_calc = min_bet
spent = min_bet
while spent <= total_money:
    print(f"{bet_calc}")
    bet_calc *= 1.5
    bet_calc = int(bet_calc + 0.5)
    spent += bet_calc
