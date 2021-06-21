"""importing the datetime module"""
import datetime

 
#Problem1                       
# defining the function

def days_in_month(year, month):    
   """functiion will return the number of days in a particular month""" 
   
   if month < 12:
       return (datetime.date(year, month+1, 1)) - (datetime.date(year, month, 1)) 
   
   else: 
       return  (datetime.date(year + 1, 1, 1)  - datetime.date(year, month, 1)) 
    
#functiion will return the number of days in a particular month
              

print(days_in_month(2020, 11))






#Problem2
#defining the function

def date_is_valid(year, month, day):
    """the function will determine if a date is valid or not"""
    
    if (datetime.date(year, month <= 12, day <= 31)):
        return True

    else:
        return False
    
#the function will print "True" if the date is vaid and "False" if otherwise
    
print(date_is_valid(1995, 12, 15))






#Problem3
#defining the function 'days between':the number of days from one date to another.

def days_in_between(year1, month1, day1, year2, month2, day2):
    """function will return the number of days between two dates"""
    
    if  (datetime.date(year2, month2, day2)) > (datetime.date(year1, month1, day1)):
        return (datetime.date(year2, month2, day2)) - datetime.date(year1, month1, day1)
    
    elif (datetime.date(year1, month1, day1)) != \
         (datetime.date(datetime.MAXYEAR - datetime.MINYEAR, month1 <= 12, day1 <= 31)):
        return 0
    
    elif (datetime.date(year2, month2, day2)) != \
         (datetime.date(datetime.MAXYEAR - datetime.MINYEAR, month2 <= 12, day2 <= 31)):
        return 0
    
    elif (datetime.date(year2, month2, day2)) < (datetime.date(year1, month1, day1)):
        return 0
    
    else:
        return None
    
    

# the function will:
# (1)return the number of days between two given dates,
# (2)return 0 if a given date is invalid
# (3)return 0 if the second date is earier than the first date.

    
    
print(days_in_between(2008, 10, 25, 2021, 2, 25))






#Problem4
#defining the function 'age in days': number of days from a past date to today's date.

def age_in_days(year, month, day):
    
   """function will print the number of days between a past date and today's date"""
    
   
   if (datetime.date(datetime.MAXYEAR - datetime.MINYEAR, month <= 12, day <= 31)):
       return (datetime.date.today()) - (datetime.date(year, month, day))
    
   elif (datetime.date(year, month, day)) != \
        (datetime.date(datetime.MAXYEAR - datetime.MINYEAR, month <= 12, day <= 31)):
       return 0
    
   elif (datetime.date(year, month, day)) > (datetime.date.today()):
       return 0
    
   else:
       return 0
    
    
print(age_in_days(2021, 11, 15))

    