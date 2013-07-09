from django.db import models

stages = [
    ("First call", "First call for comments"),
    ("First reading", "First reading"),
    ("Second reading", "Second reading"),
]

class Bill(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    # introduced_by??

class BillStage(models.Model):
    bill = models.ForeignKey(Bill)
    stage = models.CharField(choices=stages, max_length=30)

class GovInfoScraper(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_code = models.CharField(max_length=10)
    comment_startdate = models.DateField()
    comment_enddate = models.DateField()
    scrape_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return "[%s] %s" % (self.bill_code, self.bill_name)
