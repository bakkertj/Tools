import sys
import csv

n = len(sys.argv)

f = open("create_student_accounts.sh", "w" );

f.write("#!/bin/bash\n")

with open(sys.argv[1], newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         f.write("adduser -p saHW9GdxihkGQ " +  row['NetID']+"\n")

f.close();
