main.pyfrom cf_functions import ConnectFour

running = True
cf = ConnectFour()


# working on the game play
def play_game():
    while cf.running and cf.max > 0:
        cf.display()
        cf.insert()
        cf.turn = cf.switch_turn()
        cf.max -= 1

    if cf.winner:
        cf.display()
        print(f"Congratulations player {cf.winner}\nYou win!")
        return
    print(f"It's a draw, there are {cf.winner} free positions left")

play_game()