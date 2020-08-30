# Method that adjusts the each line so that escape sequence characters are 
#   recognized and are still printable in the final code
def string_adjustment(line):
  new_string = ''
  delimitters = '\'\\'
  for each_character in line:
    if each_character in delimitters:
      new_string += '\\' + each_character
    elif each_character == '\n':
      break
    else:
      new_string += each_character
    
  return new_string

# Method that reads lines from a file and then attaches the write() function
#   to it and writes it to another file.
def program_writer():
  reading_file = open('mock.py', 'r')
  writer_file = open('HW_00_Raina_Nikhil_Mentor.py','wt')

  writer_file.write('file_object = open(\'HW_00_NR_Trained.py\', \'wt\')\n')
  while True:
    line = reading_file.readline()
    if not line:
      break
    line = string_adjustment(line)
    writer_file.write('file_object.write(\''+line+'\'+\'\\n\')\n')
  writer_file.write('file_object.close()')
  writer_file.close()

if __name__ == '__main__':
  program_writer()
    