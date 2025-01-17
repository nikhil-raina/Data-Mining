"""
Name: Nikhil Raina <nxr5013@rit.edu>
FileName: HW_04_Raina_Program_446.py
Case # 446
"""

import BirdBathFunction_446_v420 as bbf
import numpy as np

if __name__ == "__main__":
    range_extender = 5
    best_fractional_volume  = bbf.BirdbathFunc446( -7.1250, 2.0000, 5.4668 )

    # The minimum and maximum range values for each parameter for the bird function
    min_params = [-30.0, -30.0, -30.0]
    max_params = [45.0, 45.0, 45.0]

    # The best values for the range values.
    # This will be changing each loop iteration in order to get the best values 
    # This will be done by reducing the range for search every loop
    # best_params = [-12.53911577994586, 8.036903507163515, 47.87125362243387]
    best_params = [-0.2, 0.2, 0.2]
    # Initial degree increment value during each iteration
    degree_increment = 10

    # value to ensure that the loop doesn't go on for too long or plays with small values
    while degree_increment > 0.5:
        rotate_min = best_params[0] - (degree_increment * range_extender)
        rotate_max = best_params[0] + (degree_increment * range_extender)
        tilt_min = best_params[1] - (degree_increment * range_extender)
        tilt_max = best_params[1] + (degree_increment * range_extender)
        twist_min = best_params[2] - (degree_increment * range_extender)
        twist_max = best_params[2] + (degree_increment * range_extender)

        if rotate_min <= min_params[0]:
            rotate_min = min_params[0]
        if rotate_max <= max_params[0]:
            rotate_max = max_params[0]
        if tilt_min <= min_params[1]:
            tilt_min = min_params[1]
        if tilt_max <= max_params[1]:
            tilt_max = max_params[1]
        if twist_min <= min_params[2]:
            twist_min = min_params[2]
        if twist_max <= max_params[2]:
            twist_max = max_params[2]


        # A nested for loop of 3 fors that checks each value within the specified range
        # for each parameter that is passed down in the Bird Bath Function.
        count = 0
        for rotate in np.arange(rotate_min, rotate_max, degree_increment):
            count += 1
            if count == 10:
                count = 0
            for tilt in np.arange(tilt_min, tilt_max, degree_increment):
                for twist in np.arange(twist_min, twist_max, degree_increment):
                    # Passes in the new parameters for the bird bath function to check the
                    # Fraction of water that is left.
                    fractional_volume = bbf.BirdbathFunc446(rotate, tilt, twist)
                    if fractional_volume > best_fractional_volume:
                        # stores the new best fractional volume and its corresponding parameters in the
                        # best params list so that it could be used for the next main iteration.
                        best_fractional_volume = fractional_volume
                        best_params = [rotate, tilt, twist]
                        print('BEST Fraction of Water = ', best_fractional_volume, '<-- Example test case results\n' )
                # print('ROTATE:', best_params[0], '\nTILT:', best_params[1], '\nTWIST:', best_params[2])
                # print('Fraction of Water = ', fractional_volume, '<-- Example test case results' )
                
        degree_increment = (degree_increment * 13) / 16
    print('ROTATE:', best_params[0], '\nTILT:', best_params[1], '\nTWIST:', best_params[2])
    print('Fraction of Water = ', best_fractional_volume, '<-- Example test case results\n' )
    print('###########################################################################################')
    # BEST fraction 0.4999855276951166
