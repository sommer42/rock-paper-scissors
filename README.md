# Rock Paper Scissors

A command-line rock-paper-scissors game in Python. Play as many rounds as you like against the computer, see a summary when you finish, and chase your high score across sessions.

## Features

- Endless rounds until you type `end`
- Short inputs (`r`, `p`, `s`) or full words (`rock`, `paper`, `scissors`)
- Input validation: invalid choices are rejected and you're asked again
- Session summary with wins, losses and draws
- Points scoring: 10 per win, 2 per draw, 0 per loss
- Play again without restarting the program
- Scores saved to `scores.json`, with a "new high score" message when you beat your record

## Requirements

- Python 3.8 or newer
- No external packages (uses only `random` and `json` from the standard library)

## How to run

```
python main.py
```

## How to play

1. Type `r`, `p` or `s` (or `rock`, `paper`, `scissors`) and press Enter.
2. The computer picks at random and the result is shown.
3. Keep playing as long as you like.
4. Type `end` to finish the session and see your results.
5. Answer `y` to start a new session or `n` to quit.

Example:

```
Choose rock (r), paper (p), scissors (s), or type end to quit:
r
Aww, you lost! I chose paper.
p
Yeppee, you won! I chose rock.
end

Nice game!

You won once.
You lost once.
We didn't draw.

Your score is 12.
```

## Scoring

| Result | Points |
| ------ | ------ |
| Win    | 10     |
| Draw   | 2      |
| Loss   | 0      |

Sessions with at least one round are saved to `scores.json` in the folder you run the game from. Delete the file to reset your history. It is listed in `.gitignore`, so it isn't uploaded to GitHub.

## Project structure

```
main.py        # the whole game
scores.json    # created automatically on first save (not tracked by Git)
LICENSE        # MIT
```

## License

Released under the [MIT License](LICENSE).
