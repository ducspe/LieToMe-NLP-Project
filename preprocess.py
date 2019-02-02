import re
import csv
new_row=[]
count = 0
with open('7Truth7LiesDataset.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    with open('cleaned_train.csv', 'w', newline='') as outtrainfile:
        for row in reader:
            count+=1
            if count > 5800:
                break
            if re.match('\s+|\n', row[-1]):
                continue
            new_row = [row[-2].strip("'|."), row[-1]]
            wr = csv.writer(outtrainfile, delimiter="\t")
            wr.writerow(new_row)
    with open('cleaned_test.csv', 'w', newline='') as outtestfile:
        for row in reader:
            if re.match('\s+|\n', row[-1]):
                continue
            new_row = [row[-2].strip("'|."), row[-1]]
            wr = csv.writer(outtestfile, delimiter="\t")
            wr.writerow(new_row)