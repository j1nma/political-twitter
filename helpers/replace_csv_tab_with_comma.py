import csv

f = open('./usernames.txt', "r")
for line in f:
    line = line.replace('\n', '')

    with open(f'../data/nonenglish_original/{line}.csv', 'r', encoding='utf-8') as f_in, open(f'../data/nonenglish_original/{line}-notabs.csv', "w", encoding='utf-8') as f_out:
        reader = csv.reader(f_in, delimiter="\t", skipinitialspace=True)
        writer = csv.writer(f_out, delimiter=",", skipinitialspace=True)
        writer.writerows(reader)