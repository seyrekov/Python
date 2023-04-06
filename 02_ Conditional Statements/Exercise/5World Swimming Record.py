# this library is needed for up (ceil) and down (floor) rounding
from math import floor

record_sec = float(input())
distance_meters = float(input())
time_one_meter_in_sec = float(input())
trace_length_time_in_sec = distance_meters * time_one_meter_in_sec
# water_obstacle = floor(water_obstacle)
water_obstacle = floor(distance_meters / 15) * 12.5

ivan_time_in_sec = trace_length_time_in_sec + water_obstacle

if ivan_time_in_sec < record_sec:
    ivan_record_in_sec = ivan_time_in_sec
    print(
        f'Yes, he succeeded! The new world record is {ivan_record_in_sec:.2f} seconds.')
else:
    ivan_record_in_sec_slower = ivan_time_in_sec - record_sec
    print(
        f'No, he failed! He was {ivan_record_in_sec_slower:.2f} seconds slower.')
