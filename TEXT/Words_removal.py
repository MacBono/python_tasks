#!/usr/bin/python3
#               "Words removal"
infile1 = './text/messy.txt'
outfile1 = './text/cleaned.txt'

delete_list = ["nigdy", " i ", "oraz", "dlaczego", "się"]
with open(infile1, encoding='UTF-8') as fin, open(outfile1, 'w+', encoding='UTF-8') as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

print(open(infile1, "r", encoding='UTF-8').read())
print(open(outfile1, "r", encoding='UTF-8').read())
