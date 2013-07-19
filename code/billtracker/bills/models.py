from django.db import models
from django.conf import settings
from model_utils.managers import InheritanceManager

class BillException(Exception):
    pass

class Bill(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    @property
    def current_stage(self):
        return BillStage.objects.filter(bill=self).order_by("-id").select_subclasses()[0]

    def __unicode__(self):
        return self.name

class BillStage(models.Model):
    bill = models.ForeignKey(Bill, related_name="stages")
    objects = InheritanceManager()

    def __unicode__(self):
        return str(self.bill)

class PreparliamentaryStage(BillStage):
    comments_start = models.DateField()
    comments_end = models.DateField()
    document_url = models.URLField(null=True, blank=True)

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
