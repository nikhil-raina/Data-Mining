import sys
import pynmea2 as nmea
import pandas as pd

kml_header = " "    # read the text file having the header txt
kml_footer = " "    
bigDataframe  = pd.DataFrame(columns=["IDen", "Time", "Latitude", "Longitutde", "Altitude"])

# TODO: Handle Parked Car
# TODO: Driving in Straight line, ignore some points
# TODO: If there is similar GPS Coords, ignore 
# TODO: If there is missing Points, cover that
# TODO: Handle case when the Car not Moving
# TODO: Find speed of the car

# this function appends string to specified file
def file_writer(file_name, str):
    file = open(file_name, "a")
    file.write(str)
    file.close()


def gpgga(msg, new_kml):
    latitude = round(msg.latitude, 6)           # latitude in 6 decimal
    longitude = round(msg.longitude, 6)         # longitude in 6 decimal
    alt = (msg.altitude)                        # altitude
    output = str(longitude) + "," + str(latitude) + "," + str(alt) + "\n"
    file_writer(new_kml, output)
    return 0

def grmc(msg):
    return 0
    
    
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
    if len(sys.argv) !=3:
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
        exit()

    gps_file, kml_file = sys.argv[1], sys.argv[2]           # get the 2 file names
    
    kml_static_text(gps_file, "helper/kml_header.txt", "helper/kml_footer.txt", kml_file)      # generates the header of the kml


    # kml_static_text (kml_file, "helper/kml_footer.txt")     # generates the footer of the kml 



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