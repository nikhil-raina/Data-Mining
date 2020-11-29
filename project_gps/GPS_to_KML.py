import sys
import pynmea2 as nmea
import pandas as pd
from preprocess_gps_data import *
import glob as g

kml_header = " "    # read the text file having the header txt
kml_footer = " "    
bigDataframe  = pd.DataFrame(columns=["IDen", "Time", "Latitude", "Longitutde", "Altitude"])

# TODO(done): Handle Parked Car
# TODO: Driving in Straight line, ignore some points
# TODO(done: not ignoring): If there is similar GPS Coords, ignore 
# TODO(done: there arent missing points so didnt have such an issue): If there is missing Points, cover that
# TODO(done: same as car being 'parked'): Handle case when the Car not Moving
# TODO(done): Find speed of the car

# this function appends string to specified file
def file_writer(file_name, str):
    file = open(file_name, "a")
    file.write(str)
    file.close()


"""
reads the data from the GPS file and returns a list.
"""
def read_gps_data(file_name):
    file = open(file_name, 'r')

    # removing the header and reading the lines
    lines = file.readlines()[5:]
    file.close()
    
    return lines


# header and footer of kml of the KML File
# def kml_static_text(kml_file, header_txt, footer_txt, new_kml):
#     header = open(header_txt, "r").read()   # reads the header of kml file
#     file_writer(new_kml, header)            # writes the header of kml file
#     with open(kml_file) as file:  
#         for _ in range(5):      # skips the first few 5 lines
#             next(file)          
#         for line in file:
#             try:
#                 msg = nmea.parse(line)
#                 splitted = line.split(",")
#                 if splitted[0] == "$GPGGA":
#                     print("GGA Sentence")
#                     gpgga(msg, new_kml)
#                 else:
#                     print("RMC sentence")
#                     grmc(msg)
#             except nmea.ParseError as e:
#                 print('Parse error: {}'.format(e))
#                 continue 
    

#     footer = open(footer_txt, "r").read()
#     file_writer(new_kml, footer)
#     print("Successfully Completed")
              

def read_all_GPS_data():
    list_of_files = g.glob('project_gps/gps_files/*_gps_file.txt')
    for gps_file in list_of_files:
        output_file = 'path_kml_files' + gps_file.split('\\')[0].split('.')[0] + '.kml'
        gps_data = read_gps_data(gps_file)
        processed_data_df = preprocessor(gps_data)
        with open(output_file, 'w') as out:
            header = open('project_gps/helper/kml_header.txt','r')
            out.write(header.read()+'\n')
            header.close()
            for data_set in processed_data_df.values.tolist():
                out.write(','.join(data_set[0:3]))
                out.write('\n')
            footer = open('headerAndFooter/kml_footer.txt', 'r')
            out.write(footer.read() + '\n')
            header.close()
            footer.close()
    print("Successfully Completed all files")




def read_input_data(gps_file, kml_file):
    gps_data = read_gps_data(gps_file)
    processed_data_df = preprocessor(gps_data)
    with open(output_file, 'w') as out:
            header = open('project_gps/helper/kml_header.txt','r')
            out.write(header.read()+'\n')
            header.close()
            for data_set in processed_data_df.values.tolist():
                out.write(','.join(data_set[0:3]))
                out.write('\n')
            footer = open('project_gps/helper/kml_footer.txt', 'r')
            out.write(footer.read() + '\n')
            header.close()
            footer.close()
    print("Successfully Completed input file")


# entry point of the program
def main():
    if len(sys.argv) != 3:
        read_all_GPS_data()
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
    else:
        read_input_data(sys.argv[1], sys.argv[2])


main()







##### Parsing

# Takes input of a coordinate and dump it to the text file
def print_coords(fileName, coord):
    return True

# reads the text file, outputs the kml file
def reader(txt_file, kml_file):
    return 0

# Detects the anomalies # maybe helper funciton?  
def anomaly_detector():
    return 0