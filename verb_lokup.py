# -*- coding: utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv

FILE_NAME = "verb_and_tense.txt"
BASE_URL = "http://dongsa.net/?search="

with open(FILE_NAME, 'rb') as f:
    row_list = []
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        row_list.append(row)
    verb_list = row_list[0]
    tense_list = row_list[1]

for verb in verb_list:
    response_list = []
    html = urlopen(BASE_URL + verb).read()
    soup = BeautifulSoup(html, "html.parser")
    conjugation_dict = {}
    for conjugation in soup.findAll("tr", {"class": "conjugation-row"}):
        type, value = map(lambda x: x.get_text(), conjugation.findAll("td"))
        conjugation_dict[type] = value
    print verb
    for tense in tense_list:
        print tense, conjugation_dict[tense]
    print

