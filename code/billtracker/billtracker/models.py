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
