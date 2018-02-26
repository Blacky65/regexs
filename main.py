import re
words = []



with open(file='text.txt') as file:
    for line in file:
        for i in line.split():
            pattern = r'((?:^|\w)*?\w{5,})'
            match = re.search(pattern, i)
            print(match)
            if match != None:
                if len(match[0]) < 6:
                    words.append(match[0])
print(words)

