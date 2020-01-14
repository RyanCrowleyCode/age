# Days In Row!
#
# This program takes as input a start day, month, and year. Then, it calculates
# the number of days total from 0 to the start date, and subtracts that number
# from the total days from 0 to the end date. It adds "1" to this to show how
# many days in a row, and it return an integer of the days in a row.
#
# This program returns how many days in a row something has occured, assuming
# that there have been no breaks in between the start date and today, and adds
# 1.
# (As in, if I started something on Monday, and did that thing Monday, Tuesday,
# and Wednesday, I would have done this 3 days in a row. But since Wednesday's
# date minus Monday's date is only 2, we add 1 for days in a row.)


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def daysBetweenDates(start_year, start_month, start_day,
                     end_year, end_month, end_day):
    total_days_start = 0
    total_days_today = 0
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # getting the total days in start_year
    for y in range(0, start_year):
        if is_leap_year(y):
            total_days_start += 366
        else:
            total_days_start += 365

    # getting the total days in month 1
    for m in range(1, start_month + 1):
        if m == 1:
            total_days_start = total_days_start
        elif m > 1:
            if is_leap_year(start_year):
                total_days_start += daysOfLeap[m-2]
            else:
                total_days_start += daysOfMonths[m-2]

    # getting the total days in start_day
    total_days_start += start_day - 1

    # getting the total days in end_year
    for y in range(0, end_year):
        if is_leap_year(y):
            total_days_today += 366
        else:
            total_days_today += 365

    # getting the total days in end_month
    for m in range(1, end_month + 1):
        if m == 1:
            total_days_today = total_days_today
        elif m > 1:
            if is_leap_year(end_year):
                total_days_today += daysOfLeap[m-2]
            else:
                total_days_today += daysOfMonths[m-2]

    # getting the total days in end_day
    total_days_today += end_day - 1

    age_in_days = total_days_today - total_days_start
    return age_in_days


def days_in_row(start_year, start_month, start_day,
                end_year, end_month, end_day):
    return daysBetweenDates(start_year, start_month, start_day, end_year,
                            end_month, end_day) + 1
