from django.db import models
from django.conf import settings

class GovInfoScraper(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_code = models.CharField(max_length=10)
    comment_startdate = models.DateField()
    comment_enddate = models.DateField()
    scrape_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    reviewed = models.BooleanField(default=False)

    def __unicode__(self):
        return "[%s] %s" % (self.bill_code, self.bill_name)

class ParliamentMinutesScraper(models.Model):
    filename = models.FileField(upload_to=settings.DIR_PARLIAMENT_MINUTES)
    house = models.CharField(max_length=20)  
    language = models.CharField(max_length=20)
    date = models.DateField()
    scrape_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    
    def __unicode__(self):
        return "%s - %s" % (self.scrape_date, self.house)
