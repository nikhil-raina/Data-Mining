from datetime import datetime
import csv


def print_name():
  print('Nikhil Raina')
  return


def personal_info():
  print('I like to act')
  return

def created_at():
  print('This file was created at 2020-08-27 18:25:34.035377')
  return


def todays_date():
  print('Current Date and Time:', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
  return


def read_and_print_csv_file():
  file = open('Data-Mining\\HW 00\\A_DATA_FILE.csv')
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


if __name__ == "__main__":
  print_name()
  personal_info()
  created_at()
  todays_date()
  read_and_print_csv_file()