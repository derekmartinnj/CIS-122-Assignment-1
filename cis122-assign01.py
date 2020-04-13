'''
Author: Derek Martin
Credit: CIS 122
Description: Introduction to programming problem set uses Python numeric data types and 
operations to solve a variety of small problems.
'''

# Question 1
total_hats = 65
cost_red = 10
total_red = total_hats // 2 # Part B bug fix: use '//' instead of '/' to omit the remainder
total_red_cost = total_red * cost_red
cost_blue = 5
total_blue = total_hats - total_red
total_blue_cost = total_blue * cost_blue
total_cost = total_red_cost + total_blue_cost
# Question 1 Part 1: Calculate total hat cost
print("Question 1 Part 1")
print("Total Hat Cost:" , total_cost)
print()

# Question 2
# Calculate steps per second, per minute, and per hour for each of the given 4 "target steps" values
target_steps = 1000
steps_hour = target_steps / 24
steps_min = steps_hour / 60
steps_sec = steps_min / 60
print("Question 2")
print("Target steps:" , target_steps)
print("Steps per second:" , steps_sec)
print("Steps per minute:" , steps_min)
print("Steps per hour:" , steps_hour)
print()
target_steps = 10000
steps_hour = target_steps / 24
steps_min = steps_hour / 60
steps_sec = steps_min / 60
print("Target steps:" , target_steps)
print("Steps per second:" , steps_sec)
print("Steps per minute:" , steps_min)
print("Steps per hour:" , steps_hour)
print()
target_steps = 20000
steps_hour = target_steps / 24
steps_min = steps_hour / 60
steps_sec = steps_min / 60
print("Target steps:" , target_steps)
print("Steps per second:" , steps_sec)
print("Steps per minute:" , steps_min)
print("Steps per hour:" , steps_hour)
print()
target_steps = 100000
steps_hour = target_steps / 24
steps_min = steps_hour / 60
steps_sec = steps_min / 60
print("Target steps:" , target_steps)
print("Steps per second:" , steps_sec)
print("Steps per minute:" , steps_min)
print("Steps per hour:" , steps_hour)
print()

# Question 3
# Determine whether my friend walked over 100 miles per week given the details of his daily tasks
# 2*Pi*r calculates the circumference of a circle
import math
radius = 200 # in feet
each_system_perimeter = 2*math.pi*radius
each_daily_distance = each_system_perimeter * 2 
total_daily_distance = each_daily_distance * 5
weekly_distance = total_daily_distance * 5
print("Question 3")
print("Weekly distance:" , weekly_distance , "feet")
print()
