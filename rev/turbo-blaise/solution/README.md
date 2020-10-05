## Solution

From challenge name and from the binary itself, it's easy to identify that the EXE file is the compiled Turbo Pascal program. One can use [DosBox](https://www.dosbox.com/) to run it.

### Password protection

On start, the program asks for a password.

Encoded passwords are stored inside the binary. Try `strings MAIN.EXE`. There are total 100 of passwords, but only 1 is correct.

There are some ways to bypass this password protection:

1. Disassemble and invert the condition, then enter the wrong password.

2. Disassemble and find the index of correct password.

3. Patch the EXE file so it will respond to a password containing 21 spaces. See [patch.py](patch.py)

4. Find the true password by manual brute-forcing :-)

### Image of the flag

After entering a correct password, the program switches to graphic mode and start to show the flag.

The only issue it shows the image very slowly. To speed up the process, one needs to increase cycles inside DosBox (press Ctrl+F12 a few times).
