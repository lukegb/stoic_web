from django.core.management.base import BaseCommand, CommandError

from apiclient.discovery import build
from dateutil.parser import parse

from website.models import Video

class Command(BaseCommand):
    can_import_settings = True

    def fetch_all_for_channel(self, channel_id, api_key):
        service = build('youtube', 'v3', developerKey=api_key)
        ss = service.search()

        def handle_page(**kwargs):
            res = ss.list(**kwargs).execute()
            if 'nextPageToken' in res:
                kwargs['pageToken'] = res['nextPageToken']
            else:
                kwargs = None
            return res['items'], kwargs

        query = {'channelId': channel_id, 'maxResults': 50, 'part': 'id,snippet'}
        while query:
            page_results, query = handle_page(**query)
            for r in page_results:
                yield r

    def handle_video(self, video):
        if video['kind'] != 'youtube#searchResult' or video['id']['kind'] != 'youtube#video':
            self.stderr.write('Got unknown thing %s - %s' % (video['kind'], video['id']['kind']))
            return

        v, created = Video.objects.get_or_create(youtube_id=video['id']['videoId'], defaults={
            'description': video['snippet']['description'],
            'title': video['snippet']['title'],
            'uploaded': parse(video['snippet']['publishedAt'])
        })
        if created:
            self.stdout.write("Imported {} (http://www.youtube.com/watch?v={})".format(video['snippet']['title'], video['id']['videoId']))

    def handle(self, *args, **kwargs):
        from django.conf import settings

        self.stdout.write("Importing videos from YouTube")
        self.stdout.write("\tChannel ID: {}".format(settings.YOUTUBE_CHANNEL_ID))

        for video in self.fetch_all_for_channel(settings.YOUTUBE_CHANNEL_ID, settings.GOOGLE_API_KEY):
            self.handle_video(video)
