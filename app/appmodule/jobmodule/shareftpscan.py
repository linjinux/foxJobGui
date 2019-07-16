#!/usr/bin/env python3
import csv
import sys
a="can.csv"
with open(a,'rt') as input_file:
    filereader = csv.reader(input_file,delimiter='\t')
    for row_list in filereader:
        if not row_list[6].strip()=='' or not row_list[8].strip()=='': 
            with open('test.csv','a+',encoding='utf-8',newline="") as f:
                f_csv = csv.writer(f)
                f_csv.writerow(row_list)
