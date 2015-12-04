# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('Contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('other', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('Contact')


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
        }
    }

    complete_apps = ['hello']