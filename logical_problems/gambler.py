# importing random module to access the random values for this program
import random
def game(goal, stake):
    WIN = 1
    LOSS = 0
    bet = 0
    win = 0
    loss = 0
    while stake < goal and stake > 0:
        spin = random.randrange(0, 2)
        if spin == WIN:
            stake +=1
            bet +=1
            win +=1
        else:
            stake -=1
            bet +=1
            loss +=1
    win_percent = (win/bet)*100
    loss_percent = (loss/bet)*100
    result = f"NUMBER OF WINS = {win}\nNUMBER OF LOSS = {loss}\nNUMBER OF BETS MADE = {bet}"+"\nPERCENTAGE OF WIN = %.2f" % win_percent +"%"+"\nPERCENTAGE OF LOSS = %.2f" % loss_percent +"%"+f"\nYOU WON ${stake}"
    return result


if __name__ == "__main__":
    g = int(input("enter the goal in terms of $ you want to achieve: "))
    s = int(input("enter the stake in $ you want to start: "))
    r = game(g, s)
    print(r)