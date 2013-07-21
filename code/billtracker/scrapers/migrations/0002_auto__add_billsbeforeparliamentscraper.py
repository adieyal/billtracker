# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BillsBeforeParliamentScraper'
        db.create_table(u'scrapers_billsbeforeparliamentscraper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('introduced_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_introduced', self.gf('django.db.models.fields.DateField')()),
            ('bill_stage', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('document_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'scrapers', ['BillsBeforeParliamentScraper'])


    def backwards(self, orm):
        # Deleting model 'BillsBeforeParliamentScraper'
        db.delete_table(u'scrapers_billsbeforeparliamentscraper')


    models = {
        u'scrapers.billsbeforeparliamentscraper': {
            'Meta': {'object_name': 'BillsBeforeParliamentScraper'},
            'bill_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bill_stage': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date_introduced': ('django.db.models.fields.DateField', [], {}),
            'document_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduced_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
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