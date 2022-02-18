#!/usr/bin/python3
import csv

outfile = "ysr_email_list"
ysrfile = "YSR-emails.csv"
emails = ""

with open(ysrfile, 'r') as infile, open(outfile, 'w') as writefile:
    csv_reader = csv.reader(infile, delimiter=',')
#    totalLines = sum(1 for row in csv_reader)
    for idx,line in enumerate(csv_reader):
        if idx > 1:
            emails = emails + ", "
        if idx != 0:
            emails = emails + line[2]
            
    writefile.write(emails)
