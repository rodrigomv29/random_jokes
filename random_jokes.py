
import pandas as pd
import matplotlib
import requests
import json
import db_jokes
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import re
import string
  
counts = dict()
joke_list = db_jokes.jokesFromTable()

def get_joke_data():
  random_jokes = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  json_data = json.loads(random_jokes.content)
  joke_data = json_data["joke"] + " -id: " + json_data["id"] 
  return joke_data

def word_count(str):
    
    words = str.split()

    for word in words:
        if word == "\n":
          continue
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def removePunctuation(s):
  punctuation = """
    !()-[]{};:'"\\\<>.?@#$%^&*_~...
  """
  newStr = ""
  for i in s:
    if i not in punctuation:
      newStr+=i 
  return newStr

def fillCounts(joke_list):
  for joke in joke_list:
    removed = removePunctuation(joke)
    word_count(removed)
  print(counts)
fillCounts(joke_list)
