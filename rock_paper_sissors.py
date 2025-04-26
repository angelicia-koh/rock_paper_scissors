import random

def rock_paper_sissors():
    player_choices = ["r", "p", "s"] 

    scored_counter = 0
    played_counter = 0
    draw_counter = 0
    lost_counter = 0

    choices_emojis = {

        "r" : "👊",
        "p" : "✋",
        "s" : "✌️",
    }

    while True:
        player_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
        played_counter += 1

        if player_choice not in player_choices:
            print("Invalid input!")
            print("Please put a valid input.")
            continue

        else:
            print("You chose", choices_emojis[player_choice])
            comp_choices = ["r", "p", "s"] 
            comp_choice = random.choice(comp_choices) 
            print("Computer chose", choices_emojis[comp_choice])

            if player_choice == "r" and comp_choice == "s":
                scored_counter += 1
                print("Yay, you won!")

            elif player_choice == "s" and comp_choice == "p":
                scored_counter += 1
                print("Yay, you won!")

            elif player_choice == "p" and comp_choice == "r":
                scored_counter += 1
                print("Yay, you won!")

            elif player_choice == comp_choice:
                draw_counter += 1
                print("It's a draw!")

            else:
                lost_counter += 1
                print("Aww, you lost.")

            while True:
                player_continue = input("Play again? y/n: ").lower()

                if player_continue == "y":
                    print("Alright, let's go!\n")
                    break # Breaks out of 'play again' loop and continues game

                elif player_continue == "n":
                    print("Okay, bye!")
                    print(f"You played {played_counter} time(s).")
                    print(f"You won {scored_counter} time(s).")
                    print(f"You lost {lost_counter} time(s).")
                    print(f"And you drew {draw_counter} time(s).\n")
                    return # Ends the function

                else:
                    print("Invalid input")


rock_paper_sissors()