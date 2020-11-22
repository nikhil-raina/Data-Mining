import sys

kml_header = " "    # read the text file having the header txt
kml_footer = " "    


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

    

def make_kml_header(kml_file):
    fileObj = open("helper/kml_header.txt", "r")
    data = fileObj.read()
    file_writer(kml_file, data)

def main():

    if len(sys.argv) !=3:
        print("Usage: python3 GPS_to_KML.py GPS_FileName.txt KML_Filename.txt")
        exit()

    gps_file, kml_file = sys.argv[1], sys.argv[2]           # get the 2 file names

    make_kml_header(kml_file)


main()