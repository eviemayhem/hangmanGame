#Evie Iles
#Sdev 220 Final Project
#Program should allow the user to play a modified version of hangman.
#Due 7/31/21

import math
import random 
import tkinter as tk
from tkinter import messagebox

counter=0
def main():
  

  def count():
    global counter
    counter += 1
#----initializes window---#
  root=tk.Tk()
  root.title("Evie Iles, Sdev 220 Final")
  root.configure(bg="black")

  guessesLeft=tk.Label(root, text="You will have seven chances to guess the word.", fg="white", bg="black")
  guessesLeft.pack()

  

  #----functions-----#

  #Reads the text file and assigns it to a list.
  def read_wordList():
    file=open("wordList.txt", "r")
    wordList=[]

    for line in file:
      for word in line.split():
        wordList.append(word)
    file.close()
    print(wordList)
    return wordList #This function has been tested and is working.
  wordList=read_wordList()

  #randomizes an item from the word list and determines length
  def define_dictionary(wordList):
    wordLength=[]
   
    #Determines the len of each word and stores in List
    for word in wordList:
      wordLength.append(len(word))
    
    #Combines both list into a dictionary for word/Length
    dictionary = {wordList[i]: wordLength[i] for i in range(len(wordList))}
    
    #Selects a random word from the dictionary 
    gameWord=random.choice(list(dictionary.items()))
    return gameWord
  
  #Splits tuple selection into two lists
  gameWord=define_dictionary(wordList)
  chosenWord, wordLen=gameWord
  print(chosenWord, wordLen)

  
  #Asks player to begin game and initializes the blank spaces
  def gameBegin(chosenWord, wordLen):
    begin=tk.messagebox.askquestion("Game Begin","Would you like to begin the game?")
    if begin =="yes":
      pass
    else:
      pass

    #----initialies rest of GUI----#
    #Canvas
    canvas=tk.Canvas(root, bg="white", height=400, width=500)
    canvas.pack(padx=10, pady=10)
  
     #Word Window
    wordShown=["_ "] * wordLen
    frame=tk.LabelFrame(root, text="Guess the word: ", width=200, bg="black", fg="white")
    frame.pack()
    word=tk.Label(frame, text=(wordShown), fg="white", bg="black")
    word.pack()

    letterGuess=tk.StringVar()
    entry=tk.Entry(root, textvariable=letterGuess)
    entry.pack()
  #grabs userGuess
    def submitGuess():
      guessedLetters=[]
      spaces=chosenWord.split()

     
      #Tells which letters have been guessed
      ghost_letters=tk.Label(root, text=guessedLetters, fg="white", bg="black")
      ghost_letters.pack()
      #grabs the user entry
      guess=entry.get()
      

      

       #----house instructions----#
  
    
    #Draws House pieces depending on guess counter. 
      def drawhouse():
        if counter==1:
          base=canvas.create_rectangle(75,250,350,400, fill="blue")
          guessesLeft.config(text=(str(counter) + "/7"))
        elif counter==2:
          points=[75,250,355,250,225,75]
          roof=canvas.create_polygon(points)
          guessesLeft.config(text=(str(counter) + "/7"))
        elif counter==3:
          door=canvas.create_rectangle(200,325,220,400, fill="brown")
          guessesLeft.config(text=(str(counter) + "/7"))
        elif counter==4:
          win1=canvas.create_rectangle(100,275,150,325, fill="white")
          guessesLeft.config(text=(str(counter) + "/7"))
        elif counter==5:
          win2=canvas.create_rectangle(275,275,325,325, fill="white")
          guessesLeft.config(text=(str(counter) + "/7"))
        elif counter==6:
          win3=canvas.create_rectangle(200,175,225,200, fill="white")
          guessesLeft.config(text=(str(counter) + "/7"))
        else:
          canvas.create_rectangle(75,375,200,400, fill="green")
          canvas.create_rectangle(220,375,350,400, fill="green")

      
      def EvalGuess(guess):
        guessedLetters=[]
        maxGuesses=7
        graveyard=tk.Label(text=guessedLetters).pack()
        if guess not in chosenWord and counter!=maxGuesses:
          count()
          drawhouse()
          guessedLetters.append(guess)
          entry.delete(0, "end")
          
        else:
          count()
          entry.delete(0, "end")
        graveyard.config(text=guessedLetters)




      
      EvalGuess(guess)   

    

    #submit button
    submit=tk.Button(root, text="Submit your guess!", command=submitGuess)
    submit.pack()
  

  gameBegin(chosenWord, wordLen)
  
  
  root.mainloop()
#----Begin Program----#
main()