# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestLog'
        db.create_table('RequestLog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')()),
            ('remote_addr', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'RequestLog'
        db.delete_table('RequestLog')


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "'Contact'"},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        u'hello.requestlog': {
            'Meta': {'object_name': 'RequestLog', 'db_table': "'RequestLog'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']