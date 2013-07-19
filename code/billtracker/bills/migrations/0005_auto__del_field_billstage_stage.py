# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BillStage.stage'
        db.delete_column(u'bills_billstage', 'stage')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'BillStage.stage'
        raise RuntimeError("Cannot reverse this migration. 'BillStage.stage' and its values cannot be restored.")

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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