import sys

def solve(year):
    if(year == 1918):
        return "26.09.1918"
    elif(year > 1918):
        day = "13"
        mnth = "09"
        yr = str(year)
        if((year%400 == 0) or ((year%4 == 0) and (year%100 != 0))):
            print('Leap Gregorian calendar system')
            day = "12"

        return day+"."+mnth+"."+yr

    else:
        day = "13"
        mnth = "09"
        yr = str(year)
        if (year % 4 == 0):
            print('Leap Julian calendar system')
            day = "12"

        return day + "." + mnth + "." + yr

year = int(input().strip())
result = solve(year)
print(result)
