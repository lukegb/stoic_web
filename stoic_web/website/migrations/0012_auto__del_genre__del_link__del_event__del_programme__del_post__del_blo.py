# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'website_genre')

        # Deleting model 'Link'
        db.delete_table(u'website_link')

        # Deleting model 'Event'
        db.delete_table(u'website_event')

        # Deleting model 'Programme'
        db.delete_table(u'website_programme')

        # Deleting model 'Post'
        db.delete_table(u'website_post')

        # Deleting model 'Blog'
        db.delete_table(u'website_blog')

        # Deleting model 'Video'
        db.delete_table(u'website_video')

        # Removing M2M table for field genre on 'Video'
        db.delete_table(db.shorten_name(u'website_video_genre'))

        # Removing M2M table for field programmes on 'Video'
        db.delete_table(db.shorten_name(u'website_video_programmes'))


    def backwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'website_genre', (
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'website', ['Genre'])

        # Adding model 'Link'
        db.create_table(u'website_link', (
            ('kind', self.gf('django.db.models.fields.CharField')(default='WW', max_length=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post', to=orm['website.Post'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['Link'])

        # Adding model 'Event'
        db.create_table(u'website_event', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Post'], unique=True, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['Event'])

        # Adding model 'Programme'
        db.create_table(u'website_programme', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'website', ['Programme'])

        # Adding model 'Post'
        db.create_table(u'website_post', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('detail', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=144, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['Post'])

        # Adding model 'Blog'
        db.create_table(u'website_blog', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 9, 0, 0))),
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.Post'], unique=True, primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(default='STOIC', max_length=40, blank=True)),
        ))
        db.send_create_signal(u'website', ['Blog'])

        # Adding model 'Video'
        db.create_table(u'website_video', (
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
        ))
        db.send_create_signal(u'website', ['Video'])

        # Adding M2M table for field genre on 'Video'
        m2m_table_name = db.shorten_name(u'website_video_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm[u'website.video'], null=False)),
            ('genre', models.ForeignKey(orm[u'website.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'genre_id'])

        # Adding M2M table for field programmes on 'Video'
        m2m_table_name = db.shorten_name(u'website_video_programmes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm[u'website.video'], null=False)),
            ('programme', models.ForeignKey(orm[u'website.programme'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'programme_id'])


    models = {
        
    }

    complete_apps = ['website']