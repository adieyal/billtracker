import requests
import re
from itertools import chain
from bs4 import BeautifulSoup
from dateutil.parser import parse
from urlparse import urljoin

url = "http://www.info.gov.za/view/DynamicAction?pageid=603&orderby=comments_by,document_date_orig,title"
#url = "http://localhost:9999/gov_info.test.html"

def scrape():
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Could not download url")
    bills = []

    soup = BeautifulSoup(r.text)
    links = soup.select(".td_list")
    links2 = soup.select(".td_list_alt")

    re_bill = re.compile(r"\w[\w\s]+Bill")

    for link in chain(links, links2):
        text = link.td.a.text.strip()
        comments = link.td.font.text.strip()
        if "bill" in text.lower():

            bill_number, datestr = comments.split(",")
            bill_number = "".join(bill_number.split())
            match = re_bill.search(text)
            if match:
                bill_name = match.group()
            else:
                bill_name = text
            
            startdate, enddate = datestr.strip().replace("comments by ", "").split(" -- ")
            startdate = parse(startdate.strip())
            enddate = parse(enddate.strip())
            document_url = urljoin(url, link.td.a["href"])

            bills.append({
                "name" : bill_name,
                "code" : bill_number,
                "startdate" : startdate,
                "enddate" : enddate,
                "url" : document_url
            })
            #print bill_name, bill_number, startdate.strip(), enddate.strip()
    return bills

if __name__ == "__main__":
    print scrape()
