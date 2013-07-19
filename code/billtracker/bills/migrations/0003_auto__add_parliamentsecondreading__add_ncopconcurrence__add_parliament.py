# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParliamentSecondReading'
        db.create_table(u'bills_parliamentsecondreading', (
            (u'billstage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bills.BillStage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'bills', ['ParliamentSecondReading'])

        # Adding model 'NCOPConcurrence'
        db.create_table(u'bills_ncopconcurrence', (
            (u'billstage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bills.BillStage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'bills', ['NCOPConcurrence'])

        # Adding model 'ParliamentPortfolioCommittee'
        db.create_table(u'bills_parliamentportfoliocommittee', (
            (u'billstage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bills.BillStage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'bills', ['ParliamentPortfolioCommittee'])

        # Adding model 'ParliamentFinalVote'
        db.create_table(u'bills_parliamentfinalvote', (
            (u'billstage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bills.BillStage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'bills', ['ParliamentFinalVote'])

        # Adding model 'ParliamentFirstReading'
        db.create_table(u'bills_parliamentfirstreading', (
            (u'billstage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bills.BillStage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'bills', ['ParliamentFirstReading'])


    def backwards(self, orm):
        # Deleting model 'ParliamentSecondReading'
        db.delete_table(u'bills_parliamentsecondreading')

        # Deleting model 'NCOPConcurrence'
        db.delete_table(u'bills_ncopconcurrence')

        # Deleting model 'ParliamentPortfolioCommittee'
        db.delete_table(u'bills_parliamentportfoliocommittee')

        # Deleting model 'ParliamentFinalVote'
        db.delete_table(u'bills_parliamentfinalvote')

        # Deleting model 'ParliamentFirstReading'
        db.delete_table(u'bills_parliamentfirstreading')


    models = {
        u'bills.bill': {
            'Meta': {'object_name': 'Bill'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bills.billstage': {
            'Meta': {'object_name': 'BillStage'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bills.Bill']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'bills.govinfoscraper': {
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
        u'bills.parliamentminutesscraper': {
            'Meta': {'object_name': 'ParliamentMinutesScraper'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'scrape_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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