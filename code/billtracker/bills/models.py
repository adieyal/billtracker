from django.db import models
from django.conf import settings
from model_utils.managers import InheritanceManager

stages = [
    ("First call", "First call for comments"),
    ("First reading", "First reading"),
    ("Second reading", "Second reading"),
]

class Bill(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    @property
    def current_stage(self):
        return BillStage.objects.filter(bill=self).order_by("-id").select_subclasses()[0]

class BillStage(models.Model):
    bill = models.ForeignKey(Bill, related_name="stages")
    stage = models.CharField(choices=stages, max_length=30)
    objects = InheritanceManager()

class PreparliamentaryStage(BillStage):
    comments_start = models.DateField()
    comments_end = models.DateField()

class ParliamentFirstReading(BillStage):
    pass

class ParliamentPortfolioCommittee(BillStage):
    pass

class ParliamentSecondReading(BillStage):
    pass

class NCOPConcurrence(BillStage):
    pass

class ParliamentFinalVote(BillStage):
    pass

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
