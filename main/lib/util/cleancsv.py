import csv
import argparse
import converter as con
from util import replaceall, try_float

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="selects this file and uses it as input")
parser.add_argument("-o", "--output", help="data will be output to this file")
args = parser.parse_args()

file = args.file
output = args.output
replacements = {"1st":"first", "2nd":"second", "-":""}

with open (file) as file_in, open (output, 'w') as file_out:
    csv_reader = csv.reader(file_in)
    csv_writer = csv.writer(file_out)
    new_rows = []

    for index, row in enumerate(csv_reader):
        if index == 0:
            for index, header in enumerate(row):
                header = replaceall(header, replacements)
                row[index] = header
            row.append("density")
            new_rows.append(row)
        elif con.get_amount_from(row[1]) is not None:
            amount = con.get_amount_from(row[1])
            density = round(float(row[0]) / con.to_volume(amount[0], amount[1]), 4)
            row.append(density)
            new_rows.append(row)
        else:
            row.append(0.0)
            new_rows.append(row)

    csv_writer.writerows(new_rows)
