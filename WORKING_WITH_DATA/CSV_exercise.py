import csv
import sys

path='./data/ceesval.csv'

while True:
    grades = list()
    with open(path, 'r', newline='') as csvfile:
        columns = ['Exam_name', 'Grade', 'Date']
        print("             ***TABLE*** ")
        reader = csv.DictReader(csvfile)
        for row in reader:
            values= list()
            print(row['Exam_name'], row['Grade'], row['Date'])
            values.append(row['Exam_name'])
            values.append(row['Grade'])
            values.append(row['Date'])
            grades.append(values)
            
    variable = input('Would you like to: 1-delete [d] 2-write [w]? ')
    if(variable=='d'):
        rec = input('record: ')
        for grade in grades:
            if rec in grade:
                grades.remove(grade)        
        with open(path, 'w', newline='') as outf:
            writer = csv.DictWriter(outf, fieldnames=columns)
            writer.writeheader()
            for row in grades:
                if row[0] != rec:
                    writer.writerow({'Exam_name' : row[0], 'Grade' : row[1], 'Date' : row[2]})
        print("             ***Record deleted***")

    elif(variable=='w'):
        with open(path, 'w', newline='') as outf:
            writer = csv.DictWriter(outf, fieldnames=columns)        
            first, second, third = input('Type: Exam_name Grade Date\n').split() 
            writer.writeheader()
            for row in grades:
                    writer.writerow({'Exam_name' : row[0], 'Grade' : row[1], 'Date' : row[2]})
            writer.writerow({'Exam_name' : first, 'Grade' : second, 'Date' : third})
        print("             ***Record added***")
    else:
        None   

    end = input('type continue or exit: ')
    if(end=='continue'):
            None
    elif(end=='exit'):
        sys.exit()
    else:
        None