import csv
import random

fileName = '../../FortuneCookieFortunes.txt'
with open(fileName, 'r') as f:
    reader = csv.reader(f)
    allRows = list(reader)
day_fortune = random.choice(allRows)[0]


