# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'posts_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=144, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('detail', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'posts', ['Post'])

        # Adding model 'Event'
        db.create_table(u'posts_event', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Post'], unique=True, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'posts', ['Event'])

        # Adding model 'Blog'
        db.create_table(u'posts_blog', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Post'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 16, 0, 0))),
            ('author', self.gf('django.db.models.fields.CharField')(default='STOIC', max_length=40, blank=True)),
        ))
        db.send_create_signal(u'posts', ['Blog'])

        # Adding model 'Link'
        db.create_table(u'posts_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('kind', self.gf('django.db.models.fields.CharField')(default='WW', max_length=2)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post', to=orm['posts.Post'])),
        ))
        db.send_create_signal(u'posts', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'posts_post')

        # Deleting model 'Event'
        db.delete_table(u'posts_event')

        # Deleting model 'Blog'
        db.delete_table(u'posts_blog')

        # Deleting model 'Link'
        db.delete_table(u'posts_link')


    models = {
        u'posts.blog': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Blog', '_ormbases': [u'posts.Post']},
            'author': ('django.db.models.fields.CharField', [], {'default': "'STOIC'", 'max_length': '40', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 16, 0, 0)'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['posts.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'posts.event': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Event', '_ormbases': [u'posts.Post']},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['posts.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'posts.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '2'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'to': u"orm['posts.Post']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'detail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '144', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['posts']