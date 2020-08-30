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

def program_writer():
  reading_file = open('Data-Mining\\HW 00\\HW_00_Raina_Nikhil\\mock.py', 'r')
  writer_file = open('Data-Mining\\HW 00\\HW_00_Raina_Nikhil\\HW_00_Raina_Nikhil_Mentor.py','wt')

  writer_file.write('file_object = open(\'Data-Mining\\\HW 00\\\HW_00_Raina_Nikhil\\\HW_00_NR_Trained.py\', \'wt\')\n')
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
    