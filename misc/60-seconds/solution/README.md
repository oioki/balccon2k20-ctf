# Solution

This puzzle is a variation of [Lights Out game](https://en.wikipedia.org/wiki/Lights_Out_(game)). We have a grid 8 x 8 cells each containing the value of 0 or 1. The goal is to set all cells to 0. The difference to classic Lights Out game is that when you select a cell in a grid, the whole row and column toggles their bits. The mathematical proof is described [here](http://www.geocities.ws/nikitadanilov/pilots/index) (it's in russian, but you can use Google Translate. In simple terms, the algorithm is:

1. Remember coordinates of all cells where the value is 1
2. Toggle all these cells (refer to the state in step #1; do not take into account current momentary state)
3. Repeat until all cells will contain 0's

There is a limit on time for the solution (60 seconds, hence the name of the challenge), therefore it's impossible to solve manually, so players have to script it. Also there is a limit on number of moves, but if you implement the algorithm described above, it should work fine.

This [solution](solution.py) implements this algorithm and gets the flag.
