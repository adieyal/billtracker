# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GovInfoScraper.reviewed'
        db.add_column(u'billtracker_govinfoscraper', 'reviewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GovInfoScraper.reviewed'
        db.delete_column(u'billtracker_govinfoscraper', 'reviewed')


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
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scrape_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'billtracker.parliamentminutesscraper': {
            'Meta': {'object_name': 'ParliamentMinutesScraper'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'scrape_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['billtracker']