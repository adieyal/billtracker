from django_cron import CronJobBase, Schedule
from scrapers.govinfo import scrape
import models

class InfoGovParser(CronJobBase):
    RUN_EVERY_MINS = 24 * 60

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = '[billtracker] InfoGov Parser'    # a unique code

    def do(self):
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
