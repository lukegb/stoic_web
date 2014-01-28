from django.contrib import admin
from django.forms import ModelForm
from website.models import Video, Programme, Blog, Event
from suit_redactor.widgets import RedactorWidget
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
class VideoAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None,                {'fields': ['youtube_id','title','description']}),
	    ('Programmes',        {'fields': ['programmes']}),
	]

class ProgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'featured','description']}),
    ]

class PostForm(ModelForm):
    class Meta:
        widgets = {
            'detail': RedactorWidget(editor_options={'lang':'en'}),
            'date': SuitSplitDateTimeWidget,
            'start_date': SuitSplitDateTimeWidget,
            'end_date': SuitSplitDateTimeWidget,
        }

class BlogAdmin(admin.ModelAdmin):
    form=PostForm
class EventAdmin(admin.ModelAdmin):
    form=PostForm

admin.site.register(Blog, BlogAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Programme,ProgAdmin)    
