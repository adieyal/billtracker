# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bill'
        db.create_table(u'billtracker_bill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'billtracker', ['Bill'])

        # Adding model 'BillStage'
        db.create_table(u'billtracker_billstage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['billtracker.Bill'])),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'billtracker', ['BillStage'])


    def backwards(self, orm):
        # Deleting model 'Bill'
        db.delete_table(u'billtracker_bill')

        # Deleting model 'BillStage'
        db.delete_table(u'billtracker_billstage')


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
        }
    }

    complete_apps = ['billtracker']