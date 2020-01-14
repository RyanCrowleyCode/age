# WELCOME TO years_months_weeks_days.py!!!
#
# This program takes 6 inputs: a starting year, month, and day, and an
# ending year, month and day.
#
# This program outputs a string that will tell the number of years, months,
# weeks, and days between the two dates. This is a great tool to print the
# age of someone as a string.
#
# This program imports datetime from the python standard library.


import datetime
now = datetime.datetime.now()

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def get_counts(year1, month1, day1, year2, month2, day2):
    ycount = 0
    mcount = 0
    wcount = 0
    dcount = 0
    count_list = []

    # years
    if month2 > month1:
        ycount = year2 - year1
    elif month2 == month1 and day2 >= day1:
        ycount = year2 - year1
    else:
        ycount = year2 - year1 - 1

    # months
    if month2 == month1:
        if day2 >= day1:
            mcount = 0
        else:
            mcount = 11
    elif month2 > month1:
        if day2 >= day1:
            mcount = month2 - month1
        else:
            mcount = month2 - month1 - 1
    elif month2 < month1:
        if day2 >= day1:
            mcount = month2 - month1 + 12
        else:
            mcount = month2 - month1 + 11

    # days
    if day2 >= day1:
        dcount = day2 - day1
    elif day2 < day1:
        if month2 == 1:
            dcount = (31 - day1) + day2
        else:
            if is_leap_year(year2):
                if day1 <= daysOfLeap[month2 - 2]:
                    dcount = (daysOfLeap[month2 - 2] - day1) + day2
                elif day1 > daysOfLeap[month2 - 2]:  # the Lucas Code
                    dcount = day2 - 1
                # else:
                #    dcount = day2
            else:
                if day1 <= daysOfMonths[month2 - 2]:
                    dcount = (daysOfMonths[month2 - 2] - day1) + day2
                elif day1 > daysOfMonths[month2 - 2]:  # the Lucas Code
                    dcount = day2 - 1

    # weeks
    if dcount >= 7:
        wcount = dcount // 7
        dcount = dcount % 7

    count_list.extend((ycount, mcount, wcount, dcount))
    return count_list


def date_string(count_list):
    ycount = count_list[0]
    mcount = count_list[1]
    wcount = count_list[2]
    dcount = count_list[3]

    to_print = ""
    final_print = ""

    if ycount > 1:
        to_print += str(ycount) + ' years'
    if ycount == 1:
        to_print += str(ycount) + ' year'
    if mcount > 1:
        if to_print != "":
            to_print += ", " + str(mcount) + ' months'
        else:
            to_print += str(mcount) + ' months'
    if mcount == 1:
        if to_print != "":
            to_print += ", " + str(mcount) + ' month'
        else:
            to_print += str(mcount) + ' month'
    if wcount > 1:
        if to_print != "":
            to_print += ", " + str(wcount) + ' weeks'
        else:
            to_print += str(wcount) + ' weeks'
    if wcount == 1:
        if to_print != "":
            to_print += ", " + str(wcount) + ' week'
        else:
            to_print += str(wcount) + ' week'
    if dcount > 1:
        if to_print != "":
            to_print += ", " + str(dcount) + ' days'
        else:
            to_print += str(dcount) + ' days'
    if dcount == 1:
        if to_print != "":
            to_print += ", " + str(dcount) + ' day'
        else:
            to_print += str(dcount) + ' day'

    final_print = to_print
    if to_print.count(',') >= 1:
        final_print = (to_print[0: to_print.rfind(',')]) + \
            ' and' + to_print[to_print.rfind(',') + 1:]

    return final_print


def years_months_weeks_days(year1, month1, day1, year2, month2, day2):
    return date_string(get_counts(year1, month1, day1, year2, month2, day2))
