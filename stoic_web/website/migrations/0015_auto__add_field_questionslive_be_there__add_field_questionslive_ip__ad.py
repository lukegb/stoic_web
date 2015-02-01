# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QuestionsLive.be_there'
        db.add_column(u'website_questionslive', 'be_there',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'QuestionsLive.ip'
        db.add_column(u'website_questionslive', 'ip',
                      self.gf('django.db.models.fields.IPAddressField')(default='8.8.8.8', max_length=15),
                      keep_default=False)

        # Adding field 'QuestionsLive.user_agent'
        db.add_column(u'website_questionslive', 'user_agent',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'QuestionsLive.be_there'
        db.delete_column(u'website_questionslive', 'be_there')

        # Deleting field 'QuestionsLive.ip'
        db.delete_column(u'website_questionslive', 'ip')

        # Deleting field 'QuestionsLive.user_agent'
        db.delete_column(u'website_questionslive', 'user_agent')


    models = {
        u'website.blog': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Blog', '_ormbases': [u'website.Post']},
            'author': ('django.db.models.fields.CharField', [], {'default': "'ICTV'", 'max_length': '40', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 1, 0, 0)'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'website.event': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Event', '_ormbases': [u'website.Post']},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'website.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
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
        u'website.questionslive': {
            'Meta': {'object_name': 'QuestionsLive'},
            'be_there': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'user_agent': ('django.db.models.fields.TextField', [], {})
        },
        u'website.video': {
            'Meta': {'ordering': "['-uploaded']", 'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['website.Genre']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programmes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['website.Programme']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['website']