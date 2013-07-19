# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParliamentMinutesScraper'
        db.create_table(u'billtracker_parliamentminutesscraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'billtracker', ['ParliamentMinutesScraper'])


    def backwards(self, orm):
        # Deleting model 'ParliamentMinutesScraper'
        db.delete_table(u'billtracker_parliamentminutesscraper')


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