#!/usr/bin/python3
#               "Words replacement"
infile1 = './text/messy.txt'
outfile2 = r'./text/replaced.txt'
diction = {" nigdy ": " prawie nigdy ",
           " i ": " oraz ",
           " oraz ": " i ",
           "dlaczego": "czemu"
           }
with open(infile1, encoding='UTF-8') as fin2, open(outfile2, 'w+', encoding='UTF-8') as fout2:
        for line in fin2:
            line = line.rstrip()
            for case in diction:
              if case in line:
                line = line.replace(case, diction[case])
            fout2.write(line)


print(open(infile1, "r", encoding='UTF-8').read())
print(open(outfile2, "r", encoding='UTF-8').read())