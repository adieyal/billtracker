"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from datetime import datetime
import models
from scrapers.models import GovInfoScraper


class TestBillStage(TestCase):
    def setUp(self):
        self.bill = models.Bill.objects.create(
            name="My bill",
            code="1234"
        )

    def test_check_that_child_creates_parent_class(self):
        models.PreparliamentaryStage.objects.create(
            bill=self.bill,
            comments_start=datetime.now(),
            comments_end=datetime.now()
        )

        self.assertEquals(models.BillStage.objects.count(), 1)

    def test_can_get_child_model_from_parent(self):

        models.PreparliamentaryStage.objects.create(
            bill=self.bill,
            comments_start=datetime.now(),
            comments_end=datetime.now()
        )

        stages = models.BillStage.objects.select_subclasses()
        for stage in stages:
            self.assertEquals(type(stage), models.PreparliamentaryStage)

    def test_current_bill_stage(self):

        models.PreparliamentaryStage.objects.create(
            bill=self.bill,
            comments_start=datetime.now(),
            comments_end=datetime.now()
        )

        models.ParliamentFirstReading.objects.create(
            bill=self.bill,
        )
        
        stage3 = models.ParliamentPortfolioCommittee.objects.create(
            bill=self.bill,
        )

        self.assertEquals(self.bill.stages.count(), 3)

        self.assertEquals(self.bill.current_stage, stage3)

class TestGovInfoScraper(TestCase):
    def setUp(self):
        self.item = GovInfoScraper.objects.create(
            bill_name="My bill",
            bill_code="1234",
            comment_startdate=datetime.now(),
            comment_enddate=datetime.now()
        )

    def test_convert_scraper_creates_bill(self):

        bill = self.item.convert_to_bill()
        self.assertEquals(type(bill), models.Bill)

        self.assertEquals(bill.name, self.item.bill_name)
        self.assertEquals(bill.code, self.item.bill_code)

    def test_convert_scraper_creates_stage(self):
        bill = self.item.convert_to_bill()
        self.assertEquals(models.BillStage.objects.count(), 1)
        stage = models.BillStage.objects.select_subclasses()[0]
        self.assertEquals(stage.bill, bill)

        self.assertEquals(bill.current_stage, stage)
        self.assertEquals(type(stage), models.PreparliamentaryStage)
