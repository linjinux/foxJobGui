#!/usr/bin/env python3
import csv
a="can.csv"
with open(a,'rt',encoding='utf-16') as input_file:
    filereader = csv.reader(input_file,delimiter='\t')
    id(filereader)
    for row_list in filereader:
        print(row_list)
        if not row_list[6].strip()=='' or not row_list[8].strip()=='': 
            with open('test.csv','a+',encoding='utf-8',newline="") as f:
                f_csv.writerow(row_list)
