import random 
import time
import subprocess

print("\rWelcome to this Memory game!!!", end="")
time.sleep(2)

class Memoryletters:
     def __init__(self, letters ):
           self.letters = letters
    
     options=("1753462020", "4123194341", "2535239732", "0753271305", "0913757315", "1439075317", "5139705133", "5133331908", "0532702353")
     random_string = random.choice(options)
   

     def printRandomLetters(self, rstring = random_string):
        for i in rstring: 
           self.letters.append(i)
           if len(self.letters) > 9:
              lettersToGuess = self.letters
              print(lettersToGuess)

correctAnswer = Memoryletters([])
lettersToGuessOn = correctAnswer.printRandomLetters()
guesses = 0
24
def guessing(): 
   user_guess_list = []
   print('\nNow try to remember what you saw!', end="")
   time.sleep(2)
   user_guess = input("Enter each number in order")
   for i in user_guess:    
       user_guess_list.append(i)
   return user_guess_list


def shuffleNumbers():
   shuffled_list = []
   for i in correctAnswer.letters:
       shuffled_list.append(i)
       random.shuffle(shuffled_list)
   return shuffled_list
   

while True:  
   print("\rPlease try to remember these numbers, and their order...", end="")
   time.sleep(2)

   print("\r", lettersToGuessOn, end="")
   time.sleep(10)
   
   subprocess.run('clear', shell=True)
   shuffled_list = shuffleNumbers()
   print("\r", shuffled_list, end="")
   user_guess_list = guessing()
   
   guesses += 1

   if user_guess_list == correctAnswer.letters: 
       print("Congratulations!! That was correct")
       print("you made", guesses ,"guesses")
       break;
   else: 
       print("the correct answer was:", correctAnswer.letters)
       print("please try again")
       