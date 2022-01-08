#!/usr/bin/env python
# coding: utf-8

# In[17]:


import warnings
warnings.filterwarnings('ignore')

get_ipython().system('pip install english-words')


# In[7]:


import random
import string
from english_words import english_words_lower_alpha_set


# In[8]:


dickey = list(english_words_lower_alpha_set)


# In[9]:


def word_choice(dicky = ['python', 'java', 'kotlin', 'javascript']):
    k = random.randrange(len(dicky))
    word_true = dicky[k]
    return word_true


# In[10]:


def check(spisok, bukva):
    
    if len(bukva) != 1:
        print("You should input a single letter")
        return spisok, 1
    
    elif bukva not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
        return spisok, 1
    
    elif bukva in spisok:
        print("You've already guessed this letter")
        return spisok, 1
    else:
        spisok.append(bukva)
        return spisok, 0


# In[13]:


def game_hangman(dickey):
    word_true = word_choice(dickey)
    
    print("H A N G M A N \n")
    
    word = len(word_true) * "-"
    
    lives = 8
    guesses = []
    
    while lives != 0:
        print(word)
        letter = input("Input a letter: ")
    
        guesses, error = check(guesses, letter)
    
        s = list(word)

        if letter in word_true:
            for j in range(len(s)):
                if (word_true[j] == letter) and (s[j] != letter):
                    s[j] = letter                
                
        elif (letter not in word_true) and (error == 0) :
            print('That letter doesn\'t appear in the word')
            lives -= 1
    
        word = "".join(s)
    
        if word == word_true:
            print("You guessed the word!")
            print("You survived!")
            break
    
        if lives == 0:
            print("You lost!")
            print("The answer is: " + word_true)
            break
        
        print('\n')


# In[15]:


start = input('Type "play" to play the game, "exit" to quit: ')
if start == "play":
    game_hangman(dickey)

