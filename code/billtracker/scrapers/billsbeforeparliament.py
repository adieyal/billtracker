import logging
import re
import string
from urlparse import urljoin
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapers import models
from dateutil import parser

class BillItem(Item):
    title = Field()
    document_number = Field()
    document_url = Field()
    introduced_by = Field()
    date_introduced = Field()
    bill_stage = Field()
    committee = Field()

url = "http://www.parliament.gov.za/live/content.php?Item_ID=605&AtoZ=%s"
class BillsBeforeParliamentSpider(CrawlSpider):
    name = "billsbeforeparliament"
    allowed_domains = ["www.parliament.gov.za"]
    start_urls = [url % letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    rules = [
        Rule(SgmlLinkExtractor(allow=['DocumentNumber=\d+']), callback='parse_bills'),
    ]

    def parse_bills(self, response):
        hxs = HtmlXPathSelector(response)
        item = BillItem()

        item["title"] = hxs.select("//b[@class='brownHeading']/text()")[0].extract()

        data = hxs.select("//table[@class='tableOrange_sep']//table[3]//td[2]/p/text()").extract()
        item["document_number"], item["date_introduced"], item["introduced_by"] = map(string.strip, data)[0:3]
        data = hxs.select("//table[@class='tableOrange_sep']//table[3]//td[2]/p/a/text()").extract()
        if len(data): item["committee"] = data[0]

        item["document_url"] = hxs.select("//a[starts-with(@href, 'commonrepository')]")[0].select("@href")[0].extract()
        item["document_url"] = urljoin(url, item["document_url"])
        item["bill_stage"] = hxs.select("//img[starts-with(@src, 'images/icon_')]").re("icon_(\d+)")[0]
        
        return item

class DBPipeline(object):
    re_code = re.compile("""
        # Typically, expect something like
        # Legal Practice Bill (B 20 - 2012), 
        ([\w\s]+)    # The title of the bill
        [(]+([^)]+)[)]+  # The code of the bill""", re.VERBOSE)

    def process_item(self, item, spider):
        title, code = DBPipeline.re_code.search(item["title"]).groups()
        if models.BillsBeforeParliamentScraper.objects.filter(bill_code=code).count() == 0:
            models.BillsBeforeParliamentScraper.objects.create(
                bill_name=title,
                bill_code=code,
                introduced_by=item["introduced_by"],
                date_introduced=parser.parse(item["date_introduced"]),
                bill_stage=item["bill_stage"],
                document_number=item["document_number"],
                url=item["document_url"],
                committee=item["committee"],
            )
        return item

def scrape():
    settings = {
        "ITEM_PIPELINES" : ["scrapers.billsbeforeparliament.DBPipeline"]
    }

    spider = BillsBeforeParliamentSpider()
    crawler = Crawler(Settings(settings))
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start(logfile="results.log", loglevel=logging.DEBUG, crawler=crawler, logstdout=False)
    reactor.run()

if __name__ == "__main__":
    scrape()
