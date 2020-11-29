import sys
import pynmea2 as nmea
import pandas as pd
from preprocess_gps_data import *
import glob as g


# TODO(done): Handle Parked Car
# TODO: Driving in Straight line, ignore some points
# TODO(done: not ignoring): If there is similar GPS Coords, ignore 
# TODO(done: there arent missing points so didnt have such an issue): If there is missing Points, cover that
# TODO(done: same as car being 'parked'): Handle case when the Car not Moving
# TODO(done): Find speed of the car


def write_to_path_kml(gps_file, processed_data_df):
    output_file = 'project_gps/path_kml_files/' + gps_file.split('\\')[1].split('.')[0] + '.kml'
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
    print('Added to ===>', output_file)
    return



def write_to_stop_kml(gps_file, stops):
    output_file = 'project_gps/stop_kml_files/' + gps_file.split('\\')[1].split('.')[0] + '.kml'
    write(output_file, 'project_gps/helper/kml_pins_header.txt')
    for stop in stops:
        write(output_file, 'project_gps/helper/stop_header.txt')
        output_file.write(str(stop[0])+','+str(stop[1]))
        output_file.write('\n')
        write(output_file, 'project_gps/helper/placemark_footer.txt')
        output_file.write('\n')
    write(output_file, 'project_gps/helper/kml_pins_footer.txt')
    

def write_to_left_right_kml(gps_file, left_turns, right_turns):
    output_file = 'project_gps/left_right_kml_files/' + gps_file.split('\\')[1].split('.')[0] + '.kml'
    with open(output_file, 'w') as output:
        header = open('project_gps/helper/kml_pins_header.txt', 'r')
        output.write(header.read() + '\n')
        header.close()
        for i in range(0, len(left_turns)):
            write(output, 'project_gps/helper/left_header.txt')
            output.write(str(left_turns[i][0])+','+str(left_turns[i][1]))
            output.write('\n')
            write(output, 'project_gps/helper/placemark_footer.txt')
            output.write('\n')

        for i in range(0, len(right_turns)):
            write(output, 'project_gps/helper/right_header.txt')
            output.write(str(right_turns[i][0]) + ',' + str(right_turns[i][1]))
            output.write('\n')
            write(output, 'project_gps/helper/placemark_footer.txt')
            output.write('\n')
        footer = open('project_gps/helper/kml_pins_footer.txt', 'r')
        output.write(footer.read() + '\n')
        footer.close()


def write(output_file, file):
    output_file.write(open(file).read())
    output_file.write("\n")


"""
reads the data from the GPS file and returns a list.
"""
def read_gps_data(file_name):
    file = open(file_name, 'r')

    # removing the header and reading the lines
    lines = file.readlines()[5:]
    file.close()
    return lines



def read_all_GPS_data():
    list_of_files = g.glob('project_gps/gps_files/*.txt')
    # list_of_files = g.glob('project_gps/gps_files/*_gps_file.txt')
    for gps_file in list_of_files:
        output_file = 'project_gps/path_kml_files/' + gps_file.split('\\')[1].split('.')[0] + '.kml'
        gps_data = read_gps_data(gps_file)
        processed_data_df = preprocessor(gps_data)
        all_stops_data = find_stops(preprocess_data_df)
        left_turns, right_turns, delta_percent = find_all_turns(gps_data)

        write_to_path_kml(gps_file, processed_data_df)



def read_input_data(gps_file, kml_file):
    gps_data = read_gps_data(gps_file)
    processed_data_df = preprocessor(gps_data)
    all_stops_data = find_stops(preprocess_data_df)
    left_turns, right_turns, delta_percent = find_all_turns(gps_data)
    
    write_to_path_kml(kml_file, processed_data_df)



# entry point of the program
def main():
    if len(sys.argv) != 3:
        read_all_GPS_data()
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
    else:
    # a = 'project_gps/kml/ZJ42_EC0_to_RIT.TXT'
    # b = 'project_gps/test_examples/test2.kml'
        read_input_data(sys.argv[1], sys.argv[2])
    # read_input_data(a, b)



if __name__ == '__main__':
    main()
