from googletrans import Translator

translator = Translator()
data = ['विनम्र श्रद्धांजलि। उन्होंने शिक्षा के क्षेत्र में अमूल्य योगदान देने', 'manzana',
        ' لغدٍ مشرق بالنماء والرخاء. سائلين']
# # so can we just replace the data with text in the .csv files??
# translator.translate(data)
# translated = translator.translate(data, dest='en')

#

for text in ['The quick brown fox', 'jumps over', 'the lazy dog']:
    translation = translator.translate(text, dest = 'ko')
    print(translation.origin, ' -> ', translation.text)


import csv
from tqdm import tqdm
import time
import datetime

accounts = [
    'Macri',
    'Kirchner'
]

def inRange(tweet, start, end):
    date = tweet[0][:10]
    s = datetime.datetime.strptime(start, "%Y-%m-%d")
    e = datetime.datetime.strptime(end, "%Y-%m-%d")
    check = datetime.datetime.strptime(date, "%Y-%m-%d")
    if s <= check <= e:
        return True
    return False

total_chars = 0
for account in tqdm(accounts):
    translator = Translator()
    translated_tweets = []
    with open(f'./data/nonenglish_original/{account}.csv') as csv_file:
        with open(f'./data/{account}-english.csv', mode='w') as file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            keys = next(csv_reader)
            writer.writerow(keys)
            translated_tweets.append(keys)
            for row in csv_reader:
                if (inRange(row, '2015-01-01', '2020-12-31')):
                    total_chars += len(row[6])
                    text = row[6]
                    trans_text = translator.translate([text], dest='en')
                    for trans in trans_text:
                        row[6] = trans.text
                    writer.writerow(row)