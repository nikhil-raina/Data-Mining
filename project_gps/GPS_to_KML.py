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

# this function appends string to specified file
def file_writer(file_name, str):
    file = open(file_name, "a")
    file.write(str)
    file.close()

    
# header and footer of kml of the KML File
def kml_static_text(kml_file, header_txt, footer_txt, new_kml):
    
    header = open(header_txt, "r").read()
    print(header)
    break


    with open(kml_file) as file:    
        for _ in range(5):      # skips the first few 5 lines
            next(file)          
        for line in file:
            try:
                msg = nmea.parse(line)
                latitude = round(msg.latitude, 6)           # latitude in 6 decimal
                longitude = round(msg.longitude, 6)         # longitude in 6 decimal
                
                try:
                    alt = (msg.altitude)                        # altitude
                    output = str(longitude) + "," + str(latitude) + "," + str(alt)   
                    print(output)
                except AttributeError as error:             # if the altitude is missing, than just continue (case: GPRMC)
                    print("Missing Altitude")
                    continue
                                
            except nmea.ParseError as e:
                print('Parse error: {}'.format(e))
                continue  
              

# entry point of the program
def main():
    if len(sys.argv) !=3:
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
        exit()

    gps_file, kml_file = sys.argv[1], sys.argv[2]           # get the 2 file names
    
    kml_static_text(gps_file, "helper/kml_header.txt", "helper/kml_footer.txt", kml_file)      # generates the header of the kml


    # kml_static_text (kml_file, "helper/kml_footer.txt")     # generates the footer of the kml 



main()

