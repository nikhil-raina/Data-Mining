import sys
import pynmea2 as nmea
import pandas as pd


def gpgga_data(data_set, process_data_frame, speed, degree):
    latitude = round(data_set.latitude, 6)          # latitude in 6 decimal
    latitude = format(latitude, ".6f")              # to add padding 0

    longitude = round(data_set.longitude, 6)        # longitude in 6 decimal
    longitude = format(longitude, ".6f")            # to add padding 0

    time = data_set.timestamp
    
    # gives format to the data that will be stored in the data frame
    rowToAppend = [speed, time, latitude, longitude, degree]
    df_size = len(process_data_frame)
    process_data_frame.loc[df_size] = rowToAppend


def gprmc_data(data_set, process_data_frame):
    latitude = round(data_set.latitude, 6)          # latitude in 6 decimal
    latitude = format(latitude, ".6f")              # to add padding 0

    longitude = round(data_set.longitude, 6)        # longitude in 6 decimal
    longitude = format(longitude, ".6f")            # to add padding 0

    time = data_set.timestamp
    speed = knots_to_miles_converter(data_set.spd_over_grnd)
    degree = data_set.true_course

    # gives format to the data that will be stored in the data frame
    rowToAppend = [longitude, latitude, speed, time, degree]
    df_size = len(process_data_frame)
    process_data_frame.loc[df_size] = rowToAppend
    return speed, degree


def knots_to_miles_converter(knots):
    return knots * 1.15078


def preprocessor(gps_data):
    speed = 0.0
    degree = 0.0
    process_data_frame  = pd.DataFrame(columns=["Longitude", "Latitude", "Speed", "Time", "Degree"])
    for data_set in gps_data:
        try:
            data_set_nmea = nmea.parse(data_set)
            if '$GPGGA' in data_set:
                print("GGA Sentence")
                gpgga_data(data_set_nmea, process_data_frame, speed, degree)
            else:
                print("RMC sentence")
                speed, degree = gprmc_data(data_set_nmea, process_data_frame)

        except nmea.ParseError as e:
            print('Parse error: {}'.format(e))
            continue 
    return process_data_frame

# def find_stops():


# def find_left():


# def find_right():

