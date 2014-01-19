from django.contrib import admin
from website.models import Video, Programme


class VideoAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None,                {'fields': ['youtube_id','title','description']}),
	    ('Programmes',        {'fields': ['programmes']}),
	]

class ProgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'featured','description']}),
    ]

admin.site.register(Video, VideoAdmin)
admin.site.register(Programme,ProgAdmin)    
