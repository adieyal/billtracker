from django.db import models
from django.conf import settings
import bills.models as bill_models

class GovInfoScraper(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_code = models.CharField(max_length=10)
    comment_startdate = models.DateField()
    comment_enddate = models.DateField()
    scrape_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    reviewed = models.BooleanField(default=False)

    def convert_to_bill(self):
        if self.reviewed:
            raise bill_models.BillException("Cannot re-convert once already converted")

        bill = bill_models.Bill.objects.create(
            name=self.bill_name,
            code=self.bill_code,
        )
        bill_models.PreparliamentaryStage.objects.create(
            bill=bill,
            comments_start=self.comment_startdate,
            comments_end=self.comment_enddate,
            document_url=self.url
        )
        self.reviewed = True
        self.save()

        return bill

    def __unicode__(self):
        return "[%s] %s" % (self.bill_code, self.bill_name)

class BillsBeforeParliamentScraper(models.Model):
    bill_name = models.CharField(max_length=100)
    bill_code = models.CharField(max_length=10)
    introduced_by = models.CharField(max_length=100)
    date_introduced = models.DateField()
    bill_stage = models.CharField(max_length=3, choices=[
        ("1", "National Assembly"),
        ("2", "NCOP"),
        ("3", "Sent to President"),
        ("4", "Finalised in an Act"),
        ("5", "Withdrawn"),
    ])
    document_number = models.CharField(max_length=10)
    url = models.URLField(null=True, blank=True)
    committee = models.CharField(max_length=100, null=True, blank=True)
    reviewed = models.BooleanField(default=False)

    # TODO - add NCOP and Presidential stages
    def convert_to_bill(self):
        if self.reviewed:
            raise bill_models.BillException("Cannot re-convert once already converted")

        try:
            bill = bill_models.Bill.objects.get(code=self.bill_code)
        except bill_models.Bill.DoesNotExist:
            bill = bill_models.Bill.objects.create(
                name=self.bill_name,
                code=self.bill_code,
            )

        bill_models.ParliamentIntroduction.objects.create(
            bill=bill,
            introduced_by=self.introduced_by,
            date_introduced=self.date_introduced,
            document_number=self.document_number,
            url=self.url
        )

        if self.committee:
            bill_models.ParliamentPortfolioCommittee.objects.create(
                bill=bill,
                committee=self.committee
            )

        self.reviewed = True
        self.save()
            
        return bill


    def __unicode__(self):
        return "[%s] %s" % (self.bill_code, self.bill_name)

    class Meta:
        verbose_name_plural = "Bills before parliament"
        verbose_name = "Bills before parliament"

class ParliamentMinutesScraper(models.Model):
    filename = models.FileField(upload_to=settings.DIR_PARLIAMENT_MINUTES)
    house = models.CharField(max_length=20)  
    language = models.CharField(max_length=20)
    date = models.DateField()
    scrape_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    
    def __unicode__(self):
        return "%s - %s" % (self.scrape_date, self.house)
