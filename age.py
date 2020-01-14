# AGE
#
# This program takes as input an 8 digit number by prompting the user. The
# numbers correspond to the year, month, and day that person was born.
#
# This program outputs how many days old the user is, and also how many years,
# months, weeks, and days old the person is as a string.
#
# This program imports datetime from the python standard library.
# This program imports days_in_row.py from the same folder as the program.
# This program imports years_months_weeks_days.py from the same folder as the
# program.

import os
import datetime

now = datetime.datetime.now()

from years_months_weeks_days import years_months_weeks_days as YMWD
from days_in_row import daysBetweenDates as DBD


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def error_screen(birthday):
    clear_screen()
    print("I'm sorry, you entered \"{}\".".format(birthday))
    print("""You must enter your birthday as 8 digits in the form of MMDDYYYY.
Please try again.""")


def date_to_numbers(date):
    separators = ["/", "-", ".", " "]  # 2/24/1964
    date_string = date
    try_date = ''

    for character in date:  # Compensates for separators in date
        if character in separators:
            char_loc = date_string.find(character)
            date_sect = date_string[:char_loc]
            if len(date_sect) == 1:
                try_date += '0' + date_sect
            else:
                try_date += date_sect
            date_string = date_string[char_loc+1:]
    try_date += date_string

    return try_date


def valid_date(date):
    try_date = date_to_numbers(date)

    if len(try_date) == 8:
        try:
            date_is_numbers = int(try_date)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


def get_date():
    good_date = False
    while not good_date:
        date = input()
        if valid_date(date):
            good_date = True
            date = date_to_numbers(date)
        else:
            error_screen(date)
            print("Please try entering your birth date again.")

    month_day_year = [int(date[:2]), int(date[2:4]), int(date[4:])]
    return month_day_year


def birthday_statement(birth_month, birth_day, birth_year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    m = months[(birth_month - 1)]

    st = [1, 21, 31]
    nd = [2, 22]
    rd = [3, 23]
    if birth_day in st:
        d = str(birth_day) + "st"
    elif birth_day in nd:
        d = str(birth_day) + "nd"
    elif birth_day in rd:
        d = str(birth_day) + "rd"
    else:
        d = str(birth_day) + "th"
    y = birth_year

    DayL = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur', 'Sun']
    day_of_week = DayL[datetime.datetime(birth_year, birth_month,
                                         birth_day).weekday()] + 'day'

    return("You were born on {}, {} {} {}.".format(day_of_week, m, d, y))


def age_inquisitor():
    clear_screen()
    print("What is your birthday?")
    print("Please enter your birthday in the form MMDDYYYY")
    birthday = get_date()
    birth_month = birthday[0]
    birth_day = birthday[1]
    birth_year = birthday[2]
    bday_sentence = birthday_statement(birth_month, birth_day, birth_year)

    clear_screen()
    days_old = DBD(birth_year, birth_month, birth_day,
                   now.year, now.month, now.day)

    age_sentence = YMWD(birth_year, birth_month, birth_day,
                        now.year, now.month, now.day)

    print(bday_sentence)
    if days_old == 1:
        print('\nYou are 1 day old. Today, people can say you were literally born yesterday!\n')
    elif days_old == 0:
        print('\nToday is your birthday, welcome to the world!\n')
    else:
        print('\nYou are {} days old.\n'.format(days_old))
        if days_old > 6:
            if now.month == birth_month and now.day == birth_day:
                print("Happy birthday! You are {} old.\n".format(age_sentence))
            else:
                print("\nThat's {} old.\n".format(age_sentence))


if __name__ == '__main__':
    age_inquisitor()
