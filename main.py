total_money = 5000
min_bet = 10

def halfs(bet, max):
    print(" ")
    print("Calculations for HALFS")
    print(" ")
    losses = 0
    round = 1
    one_zero = (37 - 18) / 37
    two_zeros = (38 - 18) / 38
    lose_chance_0 = one_zero
    lose_chance_00 = two_zeros
    while bet <= max: # while bet + losses <= max:
        print(f"---------- Round {round} ----------")
        print(f"Bet: {bet}")
        print(f"Chance to lose with 0: {lose_chance_0 * 100}%")
        print(f"Chance to lose with 00: {lose_chance_00 * 100}%")
        print(f"Total winnings: {bet * 2}")
        losses += bet
        print(f"Total spent: {losses}")
        print(f"You would win: {bet * 2 - losses}")
        bet *= 2
        print(f"Total money left: {max - losses}")
        lose_chance_0 *= one_zero
        lose_chance_00 *= two_zeros
        round += 1

def thirds(bet, max):
    print(" ")
    print("Calculations for THIRDS")
    print(" ")    
    losses = 0
    round = 1
    one_zero = (37 - 12) / 37
    two_zeros = (38 - 12) / 38
    lose_chance_0 = one_zero
    lose_chance_00 = two_zeros
    while bet <= max: # while bet + losses <= max:
        print(f"---------- Round {round} ----------")
        print(f"Bet: {bet}")
        print(f"Chance to lose with 0: {lose_chance_0 * 100}%")
        print(f"Chance to lose with 00: {lose_chance_00 * 100}%")
        print(f"Total winnings: {bet * 3}")
        losses += (bet)
        print(f"Total spent: {losses}")
        print(f"You would win: {bet * 3 - losses}")
        bet *= 1.5
        bet = int(bet + 0.5)
        print(f"Total money left: {max - losses}")
        lose_chance_0 *= one_zero
        lose_chance_00 *= two_zeros
        round += 1


halfs(min_bet, total_money)
thirds(min_bet, total_money)

print("----------HALFS----------")

bet_calc = min_bet
while bet_calc <= total_money:
    print(f"{bet_calc}")
    bet_calc *= 2
    bet_calc = int(bet_calc + 0.5)

print("----------THIRDS----------")

bet_calc = min_bet
while bet_calc <= total_money:
    print(f"{bet_calc}")
    bet_calc *= 1.5
    bet_calc = int(bet_calc + 0.5)


