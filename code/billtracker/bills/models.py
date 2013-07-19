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
