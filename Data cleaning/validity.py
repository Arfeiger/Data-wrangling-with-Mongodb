
"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import sys 
import pprint

INPUT_FILE = '/home/khalef/Workspace/Data wrangling with Mongodb/Data cleaning/autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def write_file(file,data,header):
  
  with open(file, "w") as g:
    writer = csv.DictWriter(g, delimiter=",", fieldnames = header)
    writer.writeheader()
    for row in data:
      writer.writerow(row)
  
def process_file(input_file, output_good, output_bad):
    
  bad_input  = []
  good_input = []

  with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
          #check the column productionStartYear
          start_year = row["productionStartYear"]
          uri = row ["URI"]
          if("dbpedia.org" not in uri) :
             continue
          else :
          #check if the year is between 1886-2016
            try :
              # Extract the year the the field
              year = int(start_year[:4])
              if( year > 2014 or year <1886):
                bad_input.append(row)
              else :
                good_input.append(row)
            except Exception as e :
              bad_input.append(row)
              #print("ooops!",e.__class__,"has occured")
  write_file(OUTPUT_GOOD,good_input,header)
  write_file(OUTPUT_BAD,bad_input,header)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()