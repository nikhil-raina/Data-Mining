import sys
import pynmea2 as nmea

kml_header = " "    # read the text file having the header txt
kml_footer = " "    

# TODO: Handle Parked Car
# TODO: Driving in Straight line, ignore some points
# TODO: If there is similar GPS Coords, ignore 
# TODO: If there is missing Points, cover that
# TODO: Handle case when the Car not Moving
# TODO: Find speed of the car

# Takes input of a coordinate and dump it to the text file
def print_coords(fileName, coord):
    return True

# reads the text file, outputs the kml file
def reader(txt_file, kml_file):
    return 0

# Detects the anomalies # maybe helper funciton?  
def anomaly_detector():
    return 0

# this function appends string to specified file
def file_writer(file_name, str):
    file = open(file_name, "a")
    file.write(str)
    file.close()

    
# header and footer of kml of the KML File
def kml_static_text(kml_file, static_text):
    with open(kml_file) as file:
        for _ in range(5):
            next(file)
        for line in file:
            try:
                msg = nmea.parse(line)
                msgTime = msg.timestamp
                latitude = msg.latitude
                longitude = msg.lon
                print(msg)
            except nmea.ParseError as e:
                print('Parse error: {}'.format(e))
                continue            

# entry point of the program
def main():
    if len(sys.argv) !=3:
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
        exit()

    gps_file, kml_file = sys.argv[1], sys.argv[2]           # get the 2 file names
    
    kml_static_text(gps_file, "helper/kml_header.txt")      # generates the header of the kml


    # kml_static_text (kml_file, "helper/kml_footer.txt")     # generates the footer of the kml 



main()

