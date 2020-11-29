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
    binner = 1 if len(gps_data) / 4000 < 1 else  len(gps_data) // 4000
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
    stops = []
    range_id = 3
    for idx in range(range_id+20, len(gps_data)-range_id):
        curr_data = gps_data[idx-range_id:idx+range_id]
        if curr_data[range_id][2] < 2:
            avg_before = 0
            for p_idx in range(0, range_id):
                avg_before += curr_data[p_idx][2]
            avg_before = avg_before/range_id
            avg_after = 0
            for p_idx in range(range_id+1, 2*range_id):
                avg_after += curr_data[p_idx][2]
            avg_after = avg_after / range_id

            if avg_before < 1 and avg_after > 1:
                stops.append(curr_data[range_id])
    return stops


"""
Compares two points to see if they are the same
"""
def compare_points(point1, point2, threshold=0.00005):
    lat1 = point1[1]
    lat2 = point2[1]
    lon1 = point1[0]
    lon2 = point2[0]
    lat_diff = abs(lat1 - lat2)
    lon_diff = abs(lon1 - lon2)
    if lat_diff <= threshold and lon_diff <= threshold:
        return True
    return False

"""
checks if similar point is already in the array
"""
def in_array(array, point):
    for data_point in array:
        return compare_points(data_point, point)




def find_all_turns(gps_data):
    rights, lefts = [], []
    threshold = 30
    change_percent = []
    range_check = 10
    for idx in range(range_check, len(data), range_check):
        currData, nextData = gps_data[idx], gps_data[idx-range_check]
        angle = nextData[4] - currData[4]
        abs_angle = abs(angle)
        abs_angle = (360 - abs_angle) if abs_angle > 180 else abs_angle
        sign = 1 if ((0 <= angle <= 180) or (-180 >= angle >= -360)) else -1
        angle = abs_angle * sign
        change_percent.append(angle)
        if angle > threshold:
            if not in_array(lefts,currData):
                lefts.append(currData)
        elif angle < -threshold:
            if not in_array(rights, currData):
                rights.append(currData)
    return lefts, rights, change_percent

