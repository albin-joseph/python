#It's an exersize for get better understand for functions

def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def how_many_days_in(year, month):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        if is_leap(year):
            print(f'Days in {month} is 29')
        else:
            print(f'Days in {month} is {days_in_month[month - 1]}')
    else:
        print(f'Days in {month} is {days_in_month[month - 1]}')
        
def get_days_in_a_month():
    year = int(input("Please enter year:\n")) 
    month = int(input("Please enter month:\n"))
    how_many_days_in(year,month) 
    
get_days_in_a_month()         