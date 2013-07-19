from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from billtracker import models

assert(False)
class BillTest(TestCase):
    def setUp(self):
        pass

    def test_create_bill(self):
        bill = models.Bill.objects.create(name="Test Bill", code="1234")
        self.assertTrue(bill)
