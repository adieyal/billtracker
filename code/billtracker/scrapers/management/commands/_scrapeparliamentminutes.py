import os
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from urlparse import urljoin

filedir = "files"
site_url = "http://www.parliament.gov.za/live/"
url = "http://www.parliament.gov.za/live/content.php?Category_ID=228&DocumentStart=%s"

def download_file(url, name):
    #print "Downloading: %s from %s" % (name, url)
    if not os.path.exists(filedir):
        os.mkdir(filedir)

    path = os.path.join(filedir, name)
    if os.path.exists(path):
        print "Skipped: %s" % name
        return

    r = requests.get(url)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    else:
        print "Could not download file: %s" % name

def scrape():
    for i in range(0, 200, 10):
        r = requests.get(url % i)
        
        soup = BeautifulSoup(r.text)
        table = soup.select(".tableOrange_sep")[0]
        rows = table.select("tr")[3:100:4][0:10]
        for row in rows:
            cells = row.select("td")
            filename = cells[0].text
            date = cells[2].text 
            house = cells[4].text
            language = cells[6].text
            file_url = urljoin(url, cells[10].a["href"])
            data = {
                "filename" : filename,
                "date" : parse(date),
                "house" : house,
                "language" : language,
                "url" : file_url,
            }
            download_file(file_url, filename + ".pdf")

if __name__ == "__main__":
    scrape()
