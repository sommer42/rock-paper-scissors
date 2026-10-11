import random
import json

SCORE_FILE = "scores.json"
WIN_POINTS = 10
DRAW_POINTS = 2
LOSS_POINTS = 0

beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
letter_to_name = {"r": "rock", "p": "paper", "s": "scissors"}


def load_scores():
    try:
        with open(SCORE_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_scores(history):
    with open(SCORE_FILE, "w") as f:
        json.dump(history, f)


def play_round():
    computer_choice = random.choice(list(beats))
    #print(computer_choice)

    while True:
        player_input = input().strip().lower()
        
        if player_input == "end":
            return None
        player_choice = letter_to_name.get(player_input, player_input)
        
        if player_choice in beats:
            break
        else:
            print("Please choose rock (r), paper (p), scissors (s), or type end to quit:")
    
    if player_choice == computer_choice:
        print("It's a draw! We both chose " + player_choice + ".")
        return "draw"
    
    elif beats[player_choice] == computer_choice:
        print("Yeppee, you won! I chose " + computer_choice + ".")
        return "win"
    
    else: 
        print("Aww, you lost! I chose " + computer_choice + ".")
        return "loss"


def play_session():
    score = {"win": 0, "loss": 0, "draw": 0}
    print("Choose rock (r), paper (p), scissors (s), or type end to quit:")
    while True:
        result = play_round()
        if result is None:
            break
        score[result] += 1
    return score


def show_results(score):
    points = score["win"] * WIN_POINTS + score["draw"] * DRAW_POINTS + score["loss"] * LOSS_POINTS
    
    print("")
    print("Nice game!")
    print("")

    if score["win"] == 0:
        print("You didn't win.")
    elif score["win"] == 1:
        print("You won once.")
    elif score["win"] == 2:
        print("You won twice.")
    else:
        print(f"You won {score['win']} times.")

    if score["loss"] == 0:
        print("You didn't lose.")
    elif score["loss"] == 1:
        print("You lost once.")
    elif score["loss"] == 2:
        print("You lost twice.")
    else:
        print(f"You lost {score['loss']} times.")
        
    if score["draw"] == 0:
        print("We didn't draw.")
    elif score["draw"] == 1:
        print("We drew once.")
    elif score["draw"] == 2:
        print("We drew twice.")
    else:
        print(f"We drew {score['draw']} times.")

    print("")
    print(f"Your score is {points}.")
    print("")
    
    return points


def is_new_high_score(points, history):
    old_best = max((s["points"] for s in history), default=0)
    new_record = False
    if points > old_best and history:
        new_record = True
    return new_record


def ask_play_again():
    print("Play again? (y/n):")
    while True:
        answer = input().strip().lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Please enter yes (y) or no (n):")


def main():
    history = load_scores()
    
    while True:
        print("")
        score = play_session()
        points = show_results(score)
        is_record = is_new_high_score(points, history)
        
        if sum(score.values()) > 0:
            history.append({**score, "points": points})
            save_scores(history)
        
        if is_record:
            print("That's a new high score!!")
            print("")
        
        if history:
            print(f"Best score ever: {max((s['points'] for s in history), default=0)}.")
            print("")
        
        if not ask_play_again():
            break


if __name__ == "__main__":
    main()