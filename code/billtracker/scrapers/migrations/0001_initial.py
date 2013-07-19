# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GovInfoScraper'
        db.create_table(u'scrapers_govinfoscraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bill_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('comment_startdate', self.gf('django.db.models.fields.DateField')()),
            ('comment_enddate', self.gf('django.db.models.fields.DateField')()),
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'scrapers', ['GovInfoScraper'])

        # Adding model 'ParliamentMinutesScraper'
        db.create_table(u'scrapers_parliamentminutesscraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('scrape_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'scrapers', ['ParliamentMinutesScraper'])


    def backwards(self, orm):
        # Deleting model 'GovInfoScraper'
        db.delete_table(u'scrapers_govinfoscraper')

        # Deleting model 'ParliamentMinutesScraper'
        db.delete_table(u'scrapers_parliamentminutesscraper')


    models = {
        u'scrapers.govinfoscraper': {
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
        u'scrapers.parliamentminutesscraper': {
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

    complete_apps = ['scrapers']