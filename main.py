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

def guessing(): 
   user_guess_list = []
   print('\nNow try to remember what you saw!', end="")
   time.sleep(1)
   user_guess = input("Enter each number in order")
   for i in user_guess:    
       user_guess_list.append(i)
   return user_guess_list

while True:
   shuffled_list = []
   print("\rPlease try to remember these numbers, and their order...", end="")
   time.sleep(2)

   print("\r", lettersToGuessOn, end="")
   time.sleep(10)
   
   subprocess.run('clear', shell=True)
   
   user_guess_list = guessing()
   
   guesses += 1

   if user_guess_list == correctAnswer.letters: 
       print("Congratulations!! That was correct")
       print("you made", guesses ,"guesses")
       break;
   else: 
       print("the correct answer was:", correctAnswer.letters)
       print("please try again")
       