import random 
import time
import subprocess

print("\rWelcome to this Memory game!!!", end="")
time.sleep(2)

class Memorynumbers:
     def __init__(self, numbers, active = False ):
           self.numbers = numbers
           self.active = active
    
     options=("1753462020", "4123194341", "2535239732", "0753271305", "0913757315", "1439075317", "5139705133", "5133331908", "0532702353")
     random_string = random.choice(options)
   

     def printRandomnumbers(self, rstring = random_string):
        for i in rstring: 
           self.numbers.append(i)
           if len(self.numbers) > 9:
              numbersToGuess = self.numbers
              print(numbersToGuess)
    
     def shuffleNumbers(self):
        shuffled_list = []
        for i in self.numbers:
          shuffled_list.append(i)
          random.shuffle(shuffled_list)
        return shuffled_list

     

correctAnswer = Memorynumbers([])

guesses = 0

def guessing(): 
   user_guess_list = []
   print('\nNow try to remember what you saw!', end="")
   time.sleep(2)
   user_guess = input("Enter each number in order")
   for i in user_guess:    
       user_guess_list.append(i)
   return user_guess_list
   

while True:  
   print("\rPlease try to remember these numbers, and their order...", end="")
   time.sleep(2)
   
   numbersToGuessOn = correctAnswer.printRandomnumbers()
   shuffleNumbers = correctAnswer.shuffleNumbers()

   print("\r", numbersToGuessOn, end="")
   time.sleep(10)
   
   subprocess.run('clear', shell=True)

   print("\r", shuffleNumbers, end="")
   user_guess_list = guessing()
   
   guesses += 1

   if user_guess_list == correctAnswer.numbers: 
       print("Congratulations!! That was correct!!")
       print("you made", guesses ,"guesses")
       break;
   else: 
       print("the correct answer was:", correctAnswer.numbers)
       print("please try again")
       correctAnswer.numbers = []