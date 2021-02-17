"""
Name:   Navid Nafiuzzaman
        Nikhil Raina
Filename: GPS_to_KML.py
Description: Converts NMEA GPS TXT files to KML files.
"""
import sys
import pynmea2 as nmea
import pandas as pd

kml_header = " "    # read the text file having the header txt
kml_footer = " "
bigDataframe = pd.DataFrame(
    columns=["IDen", "Time", "Latitude", "Longitutde", "Altitude"])


def file_writer(file_name, str):
    file = open(file_name, "a")
    file.write(str)
    file.close()


def gpgga(msg, new_kml):
    latitude = round(msg.latitude, 6)           # latitude in 6 decimal
    latitude = format(latitude, ".6f")          # to add padding 0

    longitude = round(msg.longitude, 6)         # longitude in 6 decimal
    longitude = format(longitude, ".6f")        # to add padding 0

    alt = (msg.altitude)                        # altitude
    curTime = msg.timestamp

    output = str(longitude) + "," + str(latitude) + "," + str(alt) + "\n"

    rowToAppend = ["$GPGGA", curTime, latitude, longitude, alt]

    cur_df_size = len(bigDataframe)
    bigDataframe.loc[cur_df_size] = rowToAppend
    file_writer(new_kml, output)


def grmc(msg):
    latitude = round(msg.latitude, 6)           # latitude in 6 decimal
    latitude = format(latitude, ".6f")          # to add padding 0

    longitude = round(msg.longitude, 6)         # longitude in 6 decimal
    longitude = format(longitude, ".6f")        # to add padding 0
    curTime = msg.timestamp

    rowToAppend = ["$GPRMC", curTime, latitude, longitude, 0]

    cur_df_size = len(bigDataframe)
    bigDataframe.loc[cur_df_size] = rowToAppend


# header and footer of kml of the KML File
def kml_static_text(kml_file, header_txt, footer_txt, new_kml):
    header = open(header_txt, "r").read()   # reads the header of kml file
    file_writer(new_kml, header)            # writes the header of kml file
    with open(kml_file) as file:
        for _ in range(5):      # skips the first few 5 lines
            next(file)
        for line in file:
            try:
                msg = nmea.parse(line)
                splitted = line.split(",")
                if splitted[0] == "$GPGGA":
                    print("GGA Sentence")
                    gpgga(msg, new_kml)
                else:
                    print("RMC sentence")
                    grmc(msg)
            except nmea.ParseError as e:
                print('Parse error: {}'.format(e))
                continue

    footer = open(footer_txt, "r").read()
    file_writer(new_kml, footer)
    print("Successfully Completed")


# entry point of the program
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
        exit()

    # get the 2 file names
    gps_file, kml_file = sys.argv[1], sys.argv[2]

    # generates the header of the kml
    kml_static_text(gps_file, "helper/kml_header.txt",
                    "helper/kml_footer.txt", kml_file)      # processes the TXT file


main()
