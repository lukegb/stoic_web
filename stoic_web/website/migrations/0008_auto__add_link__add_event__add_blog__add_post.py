# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'website_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('kind', self.gf('django.db.models.fields.CharField')(default='WW', max_length=2)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post', to=orm['website.Post'])),
        ))
        db.send_create_signal(u'website', ['Link'])

        # Adding model 'Event'
        db.create_table(u'website_event', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Post'], unique=True, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['Event'])

        # Adding model 'Blog'
        db.create_table(u'website_blog', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Post'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.CharField')(default='STOIC', max_length=40, blank=True)),
        ))
        db.send_create_signal(u'website', ['Blog'])

        # Adding model 'Post'
        db.create_table(u'website_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=144, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('detail', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'website', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'website_link')

        # Deleting model 'Event'
        db.delete_table(u'website_event')

        # Deleting model 'Blog'
        db.delete_table(u'website_blog')

        # Deleting model 'Post'
        db.delete_table(u'website_post')


    models = {
        u'website.blog': {
            'Meta': {'object_name': 'Blog', '_ormbases': [u'website.Post']},
            'author': ('django.db.models.fields.CharField', [], {'default': "'STOIC'", 'max_length': '40', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'website.event': {
            'Meta': {'object_name': 'Event', '_ormbases': [u'website.Post']},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'website.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '2'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'to': u"orm['website.Post']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'website.post': {
            'Meta': {'object_name': 'Post'},
            'detail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '144', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'website.programme': {
            'Meta': {'object_name': 'Programme'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'website.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programmes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['website.Programme']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['website']