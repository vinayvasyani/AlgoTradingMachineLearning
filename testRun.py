# -------------------YAHOO URL CONSTRUCT -------------------

from download import constructYahooFinanceURL
ticker = "^GSPC"
#format is yyyy-mm-dd
start_date = "2015-01-01"
end_date = "2016-03-01"
freq = "d"
yfURL = constructYahooFinanceURL(ticker,start_date,end_date,freq)

print (yfURL)

# --------------DOWNLOAD YAHOO FILES ------------------
# Lets try the downloader method if it works

from download import download
pathToSave = "/Users/vinay/PycharmProjects/QuantTradingWithML/Download/src/downloadedFiles/test.csv"

download(pathToSave, yfURL)


# -------------------NSE URL CONSTRUCT ----------------------
# Lets test the url for NSE

from download import constructNSEurl
nseURL = constructNSEurl("FO",1, "JUN", 2016)
#nseURL ="https://www.nseindia.com/content/historical/EQUITIES/2007/JAN/cm03JAN2007bhav.csv.zip"
print nseURL

# -------------------NSE FILE DOWNLOAD CONSTRUCT ----------------------
nseDirectory = "/Users/vinay/PycharmProjects/QuantTradingWithML/Download/src/downloadedFiles/nse/"
pathToSave = nseDirectory +"/fo1jun2016.csv.zip"
download(pathToSave, nseURL)


#-------------UNZIP THE DOWNLOADED FILE-------------
from download import  unzip
sourceFile = pathToSave
pathToExtractedFiles = nseDirectory
unzip(sourceFile,pathToExtractedFiles)

