# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import csv
import io

FILE_NAME = "verb_and_tense.txt"
BASE_URL = "https://koreanverb.app/?search="

with io.open(FILE_NAME, newline='', encoding='utf8') as f:
    row_list = []
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        row_list.append(row)
    verb_list = row_list[0]
    tense_list = row_list[1]

for verb in verb_list:
    response_list = []
    url = (BASE_URL + urllib.parse.quote(verb))
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    conjugation_dict = {}
    for conjugation in soup.findAll("tr", {"class": "conjugation-row"}):
        type, value = map(lambda x: x.get_text(), conjugation.findAll("td"))
        conjugation_dict[type] = value
    print (verb)
    for tense in tense_list:
        print(tense, conjugation_dict[tense])

