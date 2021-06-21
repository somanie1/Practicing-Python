"""
days in month
"""
def days_in_month(year, month):
    """
    days in month
    """
    import datetime
    if ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0)) and (month == 2):
        return 29
    elif (month == 2):
        return 28
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        return 30
    else:
        return 31
    date1 = datetime.date(year, month, 1)
    date2 = datetime.date(year, month+1, 1)
    delta = (date2 - date1)
    return delta.days
print(days_in_month(2010, 6))


"""
is_valid
"""
def is_valid_date(year, month, day):
    """
    is valid
    """
    import datetime

    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <= 12) and (1 <= day <= days_in_month(year, month)):
        return True
    else:
        return False
print(is_valid_date(1998, 12, 2))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    # date_first = is_valid_date(year1, month1, day1)
    # date_second = is_valid_date(year2, month2, day2)
    
    import datetime
    
    if not(is_valid_date(year1, month1, day1)) and not(is_valid_date(year2, month2, day2)):
        return 0
    elif (year2, month2, day2) < (year1, month1, day1):
        return 0
    else:
        return (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days

print(days_between(2026, 1, 3, 2025, 6, 3))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    import datetime
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    if (birthday != is_valid_date(year, month, day) and (birthday > today)):
        return 0
    else:
        # age = today.year - birthday.year
        age = today - birthday
        return age.days

print(age_in_days(2019, 7, 5))
