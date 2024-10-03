# Pythonlab_memory

## Python laboration - memory game

In this game the user get to see a list with different numbers during a limited time period. Then the user are going to remember the numbers and witch order they where in. The user can then guess until he or she guesses the right order.

This game is made in Visual studio code and Python.

### Installation

For this program I import 3 packages.

```python
import random
import time
import subprocess
```

### Instruction

Start the program by typing the following in the console:

```bash
py main.py
```

The program will then ask the user to memorize a list of numbers and their order.
The user can then type the numbers in order.

This function includes a input field for the user. Each number in the string that the user typed will be pushed to a new list called user_guess_list.

```python
def guessing():
   user_guess_list = []
   print('\nNow try to remember what you saw!', end="")
   time.sleep(1)
   user_guess = input("Enter each number in order")
   for i in user_guess:
       user_guess_list.append(i)
   return user_guess_list

```

If the user types the correct numbers and order they will get the following message: "Congratulations!! That was correct!"

This function assess if the user_guess_list and its content is the same as the content in the correctAnswer list. If so, the program prints "Congratulations!! That was correct!". The program will also break the loop and the game finishes.

If the user types the wrong answer he or she will have to guess again. That until he or she types the correct answer.

The else argument instead prints the correct answer again and invite the user to try again. If the else argument runs the while loop will not stop. The game and the while loop will run until the user guesses the correct answer.

```python
while True
###../../.
 if user_guess_list == correctAnswer.numbers: 
       print("Congratulations!! That was correct!!")
       print("you made", guesses ,"guesses")
       break;
   else: 
       print("the correct answer was:", correctAnswer.numbers)
       print("please try again")
       correctAnswer.numbers = []
```
