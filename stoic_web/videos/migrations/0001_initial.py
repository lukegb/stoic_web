# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Programme'
        db.create_table(u'videos_programme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'videos', ['Programme'])

        # Adding model 'Genre'
        db.create_table(u'videos_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'videos', ['Genre'])

        # Adding model 'Video'
        db.create_table(u'videos_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'videos', ['Video'])

        # Adding M2M table for field programmes on 'Video'
        m2m_table_name = db.shorten_name(u'videos_video_programmes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm[u'videos.video'], null=False)),
            ('programme', models.ForeignKey(orm[u'videos.programme'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'programme_id'])

        # Adding M2M table for field genre on 'Video'
        m2m_table_name = db.shorten_name(u'videos_video_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm[u'videos.video'], null=False)),
            ('genre', models.ForeignKey(orm[u'videos.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'genre_id'])


    def backwards(self, orm):
        # Deleting model 'Programme'
        db.delete_table(u'videos_programme')

        # Deleting model 'Genre'
        db.delete_table(u'videos_genre')

        # Deleting model 'Video'
        db.delete_table(u'videos_video')

        # Removing M2M table for field programmes on 'Video'
        db.delete_table(db.shorten_name(u'videos_video_programmes'))

        # Removing M2M table for field genre on 'Video'
        db.delete_table(db.shorten_name(u'videos_video_genre'))


    models = {
        u'videos.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'videos.programme': {
            'Meta': {'object_name': 'Programme'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'videos.video': {
            'Meta': {'ordering': "['-uploaded']", 'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['videos.Genre']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programmes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['videos.Programme']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['videos']