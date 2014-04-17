from django.contrib import admin
from django.forms import ModelForm
from videos.models import Video, Programme, Genre
#from suit_redactor.widgets import RedactorWidget
#from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
class VideoAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None,                {'fields': ['youtube_id','title','description', 'featured']}),
	    ('Categories',        {'fields': ['programmes', 'genre']}),
	]

class ProgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'featured','description']}),
    ]



admin.site.register(Video, VideoAdmin)
admin.site.register(Programme,ProgAdmin)    
admin.site.register(Genre)    
