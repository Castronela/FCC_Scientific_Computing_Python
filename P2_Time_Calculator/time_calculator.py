#!/bin/python3.11

def add_time(start, duration, week_day=None):
    # Setup input data
    time, meridiem = start.split(" ")
    start_h, start_m = [int(num) for num in time.split(":")]
    duration_h, duration_m = [int(num) for num in duration.split(":")]

    # Set hours and minutes
    total_hours = start_h + (start_m + duration_m) // 60 + duration_h
    hours = (total_hours - 1) % 12 + 1
    minutes = (start_m + duration_m) % 60

    # Set new meridiem
    half_days = total_hours // 12
    if half_days & 1:
        new_meridiem = 'PM' if meridiem == 'AM' else 'AM'
    else:
        new_meridiem = meridiem
    
    # Calculate days passed
    if meridiem =='PM':
        days = (half_days + 1) // 2
    else:
        days = half_days // 2

    # Build output string
    new_time = f"{hours}:{minutes:02d} {new_meridiem}"
 
    # Set week day
    if week_day:
        week_day_formated = week_day.capitalize()
        weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        week_day_index = weekdays.index(week_day_formated)
        week_day_formated = weekdays[(week_day_index + days) % 7]
        new_time += ', ' + week_day_formated

    # Set days passed
    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'
        
    return new_time

if __name__ == '__main__':
	print(add_time('6:30 PM', '205:38', 'mOnDaY'))