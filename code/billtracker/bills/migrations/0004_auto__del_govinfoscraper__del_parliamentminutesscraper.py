# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'GovInfoScraper'
        db.delete_table(u'bills_govinfoscraper')

        # Deleting model 'ParliamentMinutesScraper'
        db.delete_table(u'bills_parliamentminutesscraper')


    def backwards(self, orm):
        # Adding model 'GovInfoScraper'
        db.create_table(u'bills_govinfoscraper', (
            ('bill_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('comment_enddate', self.gf('django.db.models.fields.DateField')()),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comment_startdate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'bills', ['GovInfoScraper'])

        # Adding model 'ParliamentMinutesScraper'
        db.create_table(u'bills_parliamentminutesscraper', (
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'bills', ['ParliamentMinutesScraper'])


    models = {
        u'bills.bill': {
            'Meta': {'object_name': 'Bill'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bills.billstage': {
            'Meta': {'object_name': 'BillStage'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stages'", 'to': u"orm['bills.Bill']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'bills.ncopconcurrence': {
            'Meta': {'object_name': 'NCOPConcurrence', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'bills.parliamentfinalvote': {
            'Meta': {'object_name': 'ParliamentFinalVote', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'bills.parliamentfirstreading': {
            'Meta': {'object_name': 'ParliamentFirstReading', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'bills.parliamentportfoliocommittee': {
            'Meta': {'object_name': 'ParliamentPortfolioCommittee', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'bills.parliamentsecondreading': {
            'Meta': {'object_name': 'ParliamentSecondReading', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'bills.preparliamentarystage': {
            'Meta': {'object_name': 'PreparliamentaryStage', '_ormbases': [u'bills.BillStage']},
            u'billstage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bills.BillStage']", 'unique': 'True', 'primary_key': 'True'}),
            'comments_end': ('django.db.models.fields.DateField', [], {}),
            'comments_start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['bills']