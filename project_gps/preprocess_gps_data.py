import sys
import pynmea2 as nmea
import pandas as pd


def gpgga_data(data_set, process_data_frame, speed, degree):
    latitude = round(data_set.latitude, 6)          # latitude in 6 decimal
    latitude = format(latitude, ".6f")              # to add padding 0

    longitude = round(data_set.longitude, 6)        # longitude in 6 decimal
    longitude = format(longitude, ".6f")            # to add padding 0

    time = data_set.data[0]

    # gives format to the data that will be stored in the data frame
    rowToAppend = [longitude, latitude, str(speed), time, str(degree)]
    df_size = len(process_data_frame)
    process_data_frame.loc[df_size] = rowToAppend


def gprmc_data(data_set, process_data_frame):
    latitude = round(data_set.latitude, 6)          # latitude in 6 decimal
    latitude = format(latitude, ".6f")              # to add padding 0

    longitude = round(data_set.longitude, 6)        # longitude in 6 decimal
    longitude = format(longitude, ".6f")            # to add padding 0

    time = data_set.data[0]
    speed = str(knots_to_miles_converter(data_set.spd_over_grnd))
    degree = str(data_set.true_course)

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
    process_data_frame = pd.DataFrame(
        columns=["Longitude", "Latitude", "Speed", "Time", "Degree"])
    # This bins the data
    binner = 1 if len(gps_data) / 1000 < 1 else len(gps_data) // 1000
    for idx in range(0, len(gps_data), binner):
        data_set = gps_data[idx]
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


def find_stops(gps_data):
    stops = list()

    # since there cant be a stop sign at every point, skipping 5 data points
    range_id = 5                    # range by 5 points at every run
    for idx in range(range_id+20, len(gps_data)-range_id):
        current_data = gps_data[idx-range_id:idx+range_id]
        if float(current_data[range_id][2]) < 2:
            avg_before = 0
            for p_idx in range(0, range_id):
                avg_before += float(current_data[p_idx][2])
            avg_before /= range_id

            avg_after = 0
            for p_idx in range(range_id+1, 2*range_id):
                avg_after += float(current_data[p_idx][2])
            avg_after /= range_id

            if avg_before < 1 and avg_after > 1:            # checks the prev and curr average
                stops.append(current_data[range_id])
    return stops


"""
Compares two points and returns whether they are similar or not
"""


def to_compare(point1, point2, threshold=0.0005):
    lat1 = float(point1[1])
    lat2 = float(point2[1])
    lon1 = float(point1[0])
    lon2 = float(point2[0])

    # compares 2 points and returns if they are similar or not.
    latitude_diff = abs(lat2 - lat1)
    longitude_diff = abs(lon2 - lon1)
    if latitude_diff <= threshold and longitude_diff <= threshold:
        return True
    return False


"""
checks if similar point is already in the array
"""


def is_similar_point(array, point):
    for data in array:
        return to_compare(data, point)


def find_all_turns(gps_data):
    rights = list()
    lefts = list()

    # deciding degree factor for left and right
    threshold = 30
    delta_percent = list()

    # since there cant be a turn at every point, skipping 10 data points
    range_check = 10

    for idx in range(range_check, len(gps_data), range_check):
        current_data = gps_data[idx]
        next_data = gps_data[idx-range_check]
        angle = float(next_data[4]) - \
            float(current_data[4])      # degree difference
        abs_angle = abs(angle)                      # finds the absolute degree

        # makes sure that the angle remains in the 1st and 2nd quadrant
        abs_angle = 360 - abs_angle if abs_angle > 180 else abs_angle

        # finds the sign of the angle and implements it to the angle
        real_angle = abs_angle * \
            (1 if ((0 <= angle <= 180) or (-180 >= angle >= -360)) else -1)
        delta_percent.append(real_angle)

        # checks for similar positions and removes ignores if they are similar
        if real_angle > threshold:
            if not is_similar_point(lefts, current_data):
                lefts.append(current_data)
        elif real_angle < -threshold:
            if not is_similar_point(rights, current_data):
                rights.append(current_data)
    return lefts, rights, delta_percent
