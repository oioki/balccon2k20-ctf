# Solution

The challenge is about steganography. Given the GIF file, there are two ways the flag could be encoded there: images or the game itself.

It turns out it is possible to encode data in a chess game. Google gives this as a first result: https://incoherency.co.uk/chess-steg/index.html

Also a CLI version: https://github.com/Alheimsins/chess-steg-cli

So, we need to get a [PGN](https://en.wikipedia.org/wiki/Portable_Game_Notation) representation of the game. We could do this in at least 2 ways:

1. Convert all moves to PGN format by hand.

2. Write a program which splits the GIF into frames, analyzes frames and outputs game in PGN format.

We go with 2nd approach since it's smarter and more reliable.

We implement a simple chess OCR, and get the output for our game. First part of the solution: [solution1.py](solution1.py)

```
./solution1.py > game1.txt
```

See [game1.txt](game1.txt)

We can try to import to lichess.org, and it completes successfully. However, current representation is not complete -- marks for capturing pieces and checks are missing. But after exporting from lichess.org it is fixed. See [game2.txt](game2.txt)

Now we can try to decode this game with [chess-steg-cli](https://github.com/Alheimsins/chess-steg-cli). If we try to decode the whole game, the tool shows the error `Illegal move played??`. This could happen if we have more moves than enough to encode the message. We will try to reduce number of moves in the party and get the flag in a game with 101 moves. See [solution2.py](solution2.py) and its [output](solution2.output)
