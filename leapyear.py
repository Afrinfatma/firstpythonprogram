
year = input("Enter year to check leap year or not")
year=int(year)
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
       print ("leap year")
    else:
       print ("not a leap year")
if __name__=='__main__':
    is_leap_year(year)