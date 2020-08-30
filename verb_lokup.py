# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import csv
import io
import json
import os

os.remove("test.json")

FILE_NAME = "verb_and_tense.txt"
BASE_URL = "https://koreanverb.app/?search="

with io.open(FILE_NAME, 'r', newline='', encoding='utf8') as f:
    row_list = []
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        row_list.append(row)
    verb_list = row_list[0]
    tense_list = row_list[1]
conjugation_dict = ['[']
for verb in verb_list:
    response_list = []
    url = (BASE_URL + urllib.parse.quote(verb))
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    for conjugation in soup.findAll("tr", {"class": "conjugation-row"}):
        type, value = map(lambda x: x.get_text(), conjugation.findAll("td"))

        conjugation_dict.append('{\"Inflected\"' + ':\"' + value + '\",' + '\"dict\":[\"' + verb + '\"]}')
    # print(conjugation_dict)
# print ("List in proper method", '[%s]' % ', '.join(map(str, conjugation_dict)))
conjugation_dict.append(']')
# {"inflected":"갑니다","dict":["가다"]},
with io.open("test.json", "w", encoding='utf8') as myfile:
    myfile.write(",".join(map(str, conjugation_dict)))
# with io.open('test.json', 'w',encoding='utf8') as f:
# json.dump(conjugation_dict,f, ensure_ascii=False)
