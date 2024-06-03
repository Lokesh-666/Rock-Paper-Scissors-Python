

def pc_plays():
    import random
    pc_Plays = random.randint(1,3)
    if pc_Plays == 1:
        pc_Plays = "ROCK"
    elif pc_Plays == 2:
        pc_Plays = "PAPER"
    elif pc_Plays == 3:
        pc_Plays = "SCISSORS"
    return pc_Plays

def decideWinner(pc_Plays, Player):
    pc_Plays= pc_Plays.upper()
    Player = Player.upper()
    match pc_Plays:
        case "ROCK":
            match Player:
                case "ROCK":
                    print("It's a tie!")
                case "PAPER":
                    print("You Win!")
                    print("Keep it up!!")
                case "SCISSORS":
                    print("Ohh No, You Lost!")
                    print("Try Again")
        case "PAPER":
            match Player:
                case "ROCK":
                    print("Ohh No, You Lost!")
                    print("Try Again")
                case "PAPER":
                    print("It's a tie!")
                case "SCISSORS":
                    print("You Win!")
                    print("Keep it up!!")
        case "SCISSORS":
            match Player:
                case "ROCK":
                    print("You Win!")
                    print("Keep it up!!")
                case "PAPER":
                    print("Ohh No, You Lost!")
                    print("Try Again")
                case "SCISSORS":
                    print("It's a tie!")




def play_game():
    print("ROCK, PAPER, SCISSORS")
    PC = pc_plays()
    player = str(input("What  do you choose ( ROCK / PAPER / SCISSORS ): "))
    decideWinner(PC, player)

def main():
    print("Do you wish to play ROCK, PAPER, SCISSORS??")
    answer = str(input("Y/N?"))
    if answer.upper() =="Y":
        print("Let's Play!!")
        NumberOfGamePlays = int(input("How many times do you wish to play: "))
        i = 0
        while i < NumberOfGamePlays:
            play_game()
            i=i+1
    else:
        print("Goodbye")

if __name__ == '__main__':
    main()