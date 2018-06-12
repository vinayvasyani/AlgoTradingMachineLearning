from download import *
import time


def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return dayOfWeek, week[dayOfWeek]


listOfYears = [  2016]
listOfMonths = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
monthNumbers = range(0, 2, 1)

listOfDays = range(0, 31, 1)

pathToSave = "/Users/vinay/PycharmProjects/QuantTradingWithML/Download/src/downloadedFiles/nse/fo/"
secType = "FO"
for year in listOfYears:
    for monthInd in monthNumbers:
        for dayOfMonth in listOfDays:
            day = dayOfMonth + 1
            month = listOfMonths[monthInd]
            dateStr = str(year) + "-" + month + "-" + str(day)
            print "Starting Download for " + dateStr

            nseURL = constructNSEurl(secType, day, month, year)
            print nseURL
            saveAs = "fo" + str(day) + month + str(year) + "bhav.csv.zip"

            # weekday = weekDay(year, monthInd, day)
            isWeekend = False
            # weekday == (6, 'Saturday') or weekday == (0, 'Sunday')

            if not isWeekend and download(pathToSave + saveAs, nseURL):
                unzip(pathToSave + saveAs, pathToSave)
                time.sleep(10)
            else:
                print "Download wasn't successful for " + dateStr
                time.sleep(10)
