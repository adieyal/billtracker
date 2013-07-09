# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GovInfoScraper'
        db.create_table(u'billtracker_govinfoscraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bill_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('comment_startdate', self.gf('django.db.models.fields.DateField')()),
            ('comment_enddate', self.gf('django.db.models.fields.DateField')()),
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'billtracker', ['GovInfoScraper'])


    def backwards(self, orm):
        # Deleting model 'GovInfoScraper'
        db.delete_table(u'billtracker_govinfoscraper')


    models = {
        u'billtracker.bill': {
            'Meta': {'object_name': 'Bill'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'billtracker.billstage': {
            'Meta': {'object_name': 'BillStage'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['billtracker.Bill']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'billtracker.govinfoscraper': {
            'Meta': {'object_name': 'GovInfoScraper'},
            'bill_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bill_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comment_enddate': ('django.db.models.fields.DateField', [], {}),
            'comment_startdate': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scrape_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['billtracker']