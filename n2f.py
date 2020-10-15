#!/usr/bin/env python3

import csv
import sys
import os

def convertCSV(filename):
    with open(filename, "rt") as source, open("fa-" + os.path.basename(filename), "wt") as result:
        rdr = csv.reader(source)
        wtr = csv.writer(result, delimiter=',', )
        next(rdr)  # Skip CSV headers
        for row in rdr:
            if (row[0] == "Pending"):
                continue
            
            date = row[0]
            amount = row[2]
            description = row[1]

            if (amount[0] != "-"):
                amount = f"-{amount}"
            else:
                amount = amount[1:]

            wtr.writerow([date, amount, description])

def main(argv):
    convertCSV(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
