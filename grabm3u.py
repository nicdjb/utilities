#!/usr/bin/python3
#Grab a given m3u URL and extract just the channels I need
from os import write
import sys
import re
import requests
#import pycurl

groupTitle = [
    "\[UK\] GENERAL",
    "\[UK\] ENTERTAINMENT",
    "\[UK\] MOVIES",
    "\[US\] GENERAL",
    "\[US\] MOVIES",
    "\[US\] ENTERTAINMENT"
]

regexSearch = ""

for idx, category in enumerate(groupTitle):
    if idx > 0:
        regexSearch += "|"
    regexSearch += category

if len(sys.argv) == 1:
    print("Usage:\n{} <URL_to_file>".format(sys.argv[0]))
else:
    biglist = "biglist"
#    url = sys.argv[1]
    myUrl = "http://line.4k-eu.io/get.php?username=Sc4Cust1M&password=A6A406&type=m3u_plus&output=ts"
    keywords = re.compile(regexSearch)

#    with open(biglist,'wb') as dlFile:
#        crl = pycurl.Curl()
#        crl.setopt(crl.URL, myUrl)
#        crl.setopt(crl.WRITEDATA, dlFile)
#        crl.perform()

    outFile = "/mnt/webservers/tvfeed/myTV.m3u"
#    outFile = "myTV.m3u"

#    print("Downloading:", url)
#    urlData = requests.get(url, stream=True)
#    channels = list(urlData.text.splitlines())
    with open(biglist, 'r') as fHandle, open(outFile, 'w') as writefile:
        lines = fHandle.readlines()
        writefile.write("#EXTM3U\n")
        for idx, line in enumerate(lines):
            if keywords.search(line):
                newline = line[:line.find(',')] + ' tvg-shift="+1"' + line[line.find(','):]
                writefile.write(newline)
                writefile.write(lines[idx+1])
