from datetime import datetime
import csv

# Method is responsible to print out the name of the creator of the code file
def print_name():
  print('Nikhil Raina')
  return

# Method prints out a simple personal fact about the creator of the code file
def personal_info():
  print('I like to act')
  return

# Method that prints the date of the code file when it was completely done 
def created_at():
  print('This file was created at 2020-08-27 18:25:34.035377')
  return

# Method that prints the current date
def todays_date():
  print('Current Date and Time:', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
  return

# Method that does a little pre-processing on the CSV file
#   and then prints out the number of rows and columns.
def read_and_print_csv_file():
  file = open('A_DATA_FILE.csv')
  csv_reader = csv.reader(file, delimiter=',')
  row_counter = 0
  column_counter = 0
  column_counter_flag = True
  header_str = 'HeaderForCol'
  for row_data_set in csv_reader:
    if len(row_data_set) > 0:
      if header_str not in row_data_set[0]:
        for cell in row_data_set:
          if len(cell) > 0:
              if cell.strip() != ' ':
                if(column_counter_flag):
                  column_counter += 1
        column_counter_flag = False
        row_counter += 1
  
  print('columns:', column_counter)
  print('rows:', row_counter)
  file.close()
  return

# Main method to call the other functions
if __name__ == "__main__":
  print_name()
  personal_info()
  created_at()
  todays_date()
  read_and_print_csv_file()