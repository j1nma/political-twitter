commands = []
f = open('./usernames.txt', "r")
for line in f:
  line = line.replace('\n', '')
  commands.append(f'touch ./out/{line}.csv\n')
  commands.append(f'twint -u "{line}" --since "2016-01-01" --until "2020-12-31" --csv -o ./out/{line}.csv --tabs\n')
