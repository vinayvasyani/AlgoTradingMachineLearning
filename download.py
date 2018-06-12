# MODULE TO CONSTRUCT URLS AND DOWNLOAD FILES FROM YAHOO FINANCE AND NSE INDIA WEBSITE.


# Method to construct download url for the ticker (historic) information file.
# example :
# Daily: ^GSPC ; DAILY; 03-01-1950 to 05-17-2016
# http://finance.yahoo.com/q/hp?s=%5EGSPC&a=00&b=3&c=1950&d=05&e=17&f=2016&g=d

# Weekly: ^GSPC ; MONTHLY 03-01-1950 to 05-17-2016
# http://finance.yahoo.com/q/hp?s=%5EGSPC&a=00&b=3&c=1950&d=05&e=17&f=2016&g=w

# Monthly: ^GSPC ; DAILY; 03-01-1950 to 05-17-2016
# http://finance.yahoo.com/q/hp?s=%5EGSPC&a=00&b=3&c=1950&d=05&e=17&f=2016&g=m
from datetime import datetime;

def constructYahooFinanceURL(ticker, start_date, end_date, freq):
    # convert start and end date strings to date time objects so we can extract components
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    s = ticker.replace("^", "%5E")

    # extract out strings from date for url construction.
    # a and b represent month and day of start date.
    # c and d represent month and day of end date.

    # month - starts with index 0 and its two characters
    # 0-9 are covered, any month above 10 will be two digits
    if (start_date.month - 1 < 10):
        a = "0" + str(start_date.month - 1)
    else:
        a = str(start_date.month - 1)

    # day - starts with index 1 and its two characters
    # 1-9 are covered, any month above 10 will be two digits
    if (start_date.day < 10):
        b = "0" + str(start_date.day)
    else:
        b = str(start_date.day)

    c = str(start_date.year)

    # month - starts with index 0 and its two characters
    # 0-9 are covered, any month above 10 will be two digits
    if (end_date.month - 1 < 10):
        d = "0" + str(end_date.month - 1)
    else:
        d = str(end_date.month - 1)

    # day - starts with index 1 and its two characters
    # 1-9 are covered, any month above 10 will be two digits
    if (end_date.day < 10):
        e = "0" + str(end_date.day)
    else:
        e = str(end_date.day)

    f = str(end_date.year)

    # g is the frequency daily/monthly/yearly
    g = freq

    # Finally lets construct the url.

    # yfURL = "http://finance.yahoo.com/q/hp?s=" + s + "&a=" + a + "&b=" + b + "&c=" + c + "&d=" + d + "&e=" + e + "&f=" + f + "&g=" + g
    yfURL = "http://real-chart.finance.yahoo.com/table.csv?s=" + s + "&a=" + a + "&b=" + b + "&c=" + c + "&d=" + d + "&e=" + e + "&f=" + f + "&g=" + g

    return yfURL


# Method to construct download url for the ticker (historic) information file.
def download(filePath, downloadUrl):
    import urllib2

    # NSE INDIA website needs to feel that a manual user is donwloading, hence we pass the user agent details
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept': '*/*',
        'Host': 'www.nseindia.com',
        'Referer': 'https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'keep-alive'}

    webRequest = urllib2.Request(downloadUrl, headers=hdr)
    try:
        page = urllib2.urlopen(webRequest)

        # download the content
        content = page.read()

        # open the binary streamwriter to file where we want to save contents
        with open(filePath, "wb") as output:
            output.write(bytearray(content))

        return True

            # note that we are just downloaoding the contents and writing to file.
            # This way we are actually agnostic to what kind of file it is - csv/zip/excel

    except urllib2.HTTPError, e:
        print e.fp.read()
        return False


# Method to construct download url from NSE India website.

# Cash Markets:
# https://www.nseindia.com/content/historical/EQUITIES/2016/JUN/cm01JUN2016bhav.csv.zip

# Future Options markets:
# https://www.nseindia.com/content/historical/DERIVATIVES/2016/JUN/fo01JUN2016bhav.csv.zip
# month would be 3 day char eg. MAY, JUN, AUG ..
def constructNSEurl(secType, day, month, year):
    if (day < 10):
        day = "0" + str(day)
    else:
        day = str(day)

    year = str(year)
    #https://www.nseindia.com/content/historical/EQUITIES/2007/JAN/cm03JAN2007bhav.csv.zip
    if secType == "CM":
        nseUrl = "https://www.nseindia.com/content/historical/EQUITIES/" + year + "/" + month + "/cm" + day + month + year + "bhav.csv.zip"
    elif secType == "FO":
        nseUrl = "https://www.nseindia.com/content/historical/DERIVATIVES/" + year + "/" + month + "/fo" + day + month + year + "bhav.csv.zip"
    else:
        nseUrl = ""

    return nseUrl


def unzip (pathOfZipFile, pathOfExtractedFile):
    import os
    extractedFiles = [];
    if os.path.exists (pathOfZipFile):
        with open(pathOfZipFile, "rb") as fh:
            import zipfile
            zipFileHandler = zipfile.ZipFile(fh)

            for name in zipFileHandler.namelist():
                zipFileHandler.extract(name,pathOfExtractedFile)
                extractedFiles.append(pathOfExtractedFile+name)
        print "Extracted " + str(len(extractedFiles) -1) + " from " + pathOfZipFile

