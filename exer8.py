
def is_leap_year (year):
    if year%4 == 0:
     if year%100 == 0:
            if year%400 !=0:
                return(f"{year} is not a leap year")
     return(f"{year} is a leap year")
    else:
     return(f"{year} is not a leap year")

year = int(input("Input year: "))
print(is_leap_year(year))
