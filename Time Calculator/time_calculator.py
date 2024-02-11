def add_time(start, duration, start_day=None):
    # Parsing start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Parsing duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Converting start time to 24-hour format
    if period == 'PM':
        start_hour += 12

    # Adding duration
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Handling overflow in minutes
    end_hour += end_minute // 60
    end_minute %= 60

    # Handling overflow in hours
    days_passed = end_hour // 24
    end_hour %= 24

    # Determining period (AM or PM) for the end time
    end_period = 'AM' if end_hour < 12 else 'PM'
    if end_hour >= 12:
        end_hour -= 12
    if end_hour == 0:
        end_hour = 12

    # Adding day(s)
    days_later = ''
    if days_passed == 1:
        days_later = ' (next day)'
    elif days_passed > 1:
        days_later = f' ({days_passed} days later)'

    # Determining the new day of the week if start_day is provided
    new_day = ''
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_passed) % 7
        new_day = f', {days_of_week[new_day_index]}'

    # Constructing the result string
    new_time = f"{end_hour if end_hour != 0 else 12}:{end_minute:02} {end_period}{new_day}{days_later}"

    return new_time
