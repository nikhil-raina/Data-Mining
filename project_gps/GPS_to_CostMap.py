"""
Name:   Navid Nafiuzzaman
        Nikhil Raina
Filename: GPS_to_CostMap.py
Description: Converts NMEA GPS TXT files to Cost map KML files
"""
import sys
import pandas as pd
from preprocess_gps_data import preprocessor, find_stops, find_all_turns
import glob as g


# Write the path of the KML files


def write_to_path_kml(gps_file, processed_data_df):
    output_file = '/path_kml_files/' + \
        gps_file.split('\\')[1].split('.')[0] + '.kml'
    with open(output_file, 'w') as out:
        header = open('/helper/kml_header.txt', 'r')
        out.write(header.read()+'\n')
        header.close()
        for data_set in processed_data_df:
            out.write(','.join(data_set[0:3]))
            out.write('\n')
        footer = open('/helper/kml_footer.txt', 'r')
        out.write(footer.read() + '\n')
        header.close()
        footer.close()
    print('Added to ===>', output_file)
    return

# Writes the Stop KML files


def write_to_stop_kml(out, stops):
    read_and_write(out, '/helper/kml_pins_header.txt')
    for stop in stops:
        read_and_write(out, '/helper/stop_header.txt')
        out.write(stop[0] + ',' + stop[1] + '\n')
        read_and_write(out, '/helper/placemark_footer.txt')
        out.write('\n')
    read_and_write(out, '/helper/kml_pins_footer.txt')
    print('Added to ===>', out)
    return

# Writes the Left Right KML Files


def write_to_left_right_kml(gps_file, left_turns, right_turns):
    output_file = '/left_right_kml_files/' + \
        gps_file.split('\\')[1].split('.')[0] + '.kml'
    with open(output_file, 'w') as out:
        header = open('/helper/kml_pins_header.txt', 'r')
        out.write(header.read() + '\n')
        for i in range(0, len(left_turns)):
            read_and_write(out, '/helper/left_header.txt')
            out.write(left_turns[i][0] + ',' + left_turns[i][1] + '\n')
            read_and_write(out, '/helper/placemark_footer.txt')
            out.write('\n')

        for i in range(0, len(right_turns)):
            read_and_write(out, '/helper/right_header.txt')
            out.write(right_turns[i][0] + ',' + right_turns[i][1] + '\n')
            read_and_write(out, '/helper/placemark_footer.txt')
            out.write('\n')
        footer = open('/helper/kml_pins_footer.txt', 'r')
        out.write(footer.read() + '\n')
        footer.close()
        header.close()
    print('Added to ===>', output_file)
    return


# Rights the file
def read_and_write(output_file, file):
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
    # list_of_files = g.glob('/gps_files/*.txt')
    list_of_files = g.glob('/gps_files/*_gps_file.txt')
    for gps_file in list_of_files:
        output_file = '/path_kml_files/' + \
            gps_file.split('\\')[1].split('.')[0] + '.kml'
        gps_data = read_gps_data(gps_file)
        processed_data_df = preprocessor(gps_data)
        all_stops_data = find_stops(processed_data_df.values.tolist())
        left_turns, right_turns, delta_percent = find_all_turns(
            processed_data_df.values.tolist())

        # writes the kml data on to the corresponding files
        write_to_path_kml(gps_file, processed_data_df.values.tolist())
        write_to_left_right_kml(gps_file, left_turns, right_turns)
        with open('/stop_kml_files/' + gps_file.split('\\')[1].split('.')[0] + '.kml', 'w') as out:
            write_to_stop_kml(out, all_stops_data)


def read_input_data(gps_file, kml_file):
    gps_data = read_gps_data(gps_file)
    processed_data_df = preprocessor(gps_data)
    all_stops_data = find_stops(processed_data_df.values.tolist())
    left_turns, right_turns, delta_percent = find_all_turns(
        processed_data_df.values.tolist())

    # writes the kml data on to the corresponding files
    write_to_path_kml(gps_file, processed_data_df.values.tolist())
    write_to_left_right_kml(gps_file, left_turns, right_turns)
    write_to_stop_kml(gps_file, all_stops_data)


# entry point of the program
def main():
    if len(sys.argv) != 3:
        read_all_GPS_data()
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
    else:
        # a = '/kml/ZJ42_EC0_to_RIT.TXT'
        # b = '/test_examples/test2.kml'
        read_input_data(sys.argv[1], sys.argv[2])
    # read_input_data(a, b)


if __name__ == '__main__':
    main()
