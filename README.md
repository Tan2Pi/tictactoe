# tictactoe
Play tic-tac-toe versus an A.I.!

## Implementation
Text based tic-tac-toe was implemented using python and the alpha-beta variation of the minimax algorithm

## Issues
I spent a lot of time working on developing and debugging a game tree which ended up being unnecessary for this project. My board class is also not currently being used in my alphabeta function, because it results in reference issues (should pass-by-value). I didn't anticipate this issue, but as a result redundant code had to be added to accommodate the alphabeta function parameter `board`, which is a 2D list, rather than a class object with access to class methods.

## Future Work
The next immediate step will be to rewrite code to reduce redundancies and improve cohesiveness with the alphabeta function. In the future, I'd like to implement [Ultimate tic-tac-toe](https://docs.riddles.io/ultimate-tic-tac-toe/rules), which will use this code as a base.