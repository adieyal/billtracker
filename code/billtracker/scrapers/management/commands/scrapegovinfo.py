from django.core.management.base import BaseCommand, CommandError
from scrapers.govinfo import scrape
import scrapers.models as models

class Command(BaseCommand):
    def handle(self, *args, **options):
        results = scrape()
        for r in results:
            url = r["url"]
            if models.GovInfoScraper.objects.filter(url=url).count() == 0:
                models.GovInfoScraper.objects.create(
                    bill_name=r["name"],
                    bill_code=r["code"],
                    comment_startdate=r["startdate"],
                    comment_enddate=r["enddate"],
                    url=r["url"],
                )
                print r
