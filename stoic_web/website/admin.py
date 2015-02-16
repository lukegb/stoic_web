from django.contrib import admin
from django.forms import ModelForm
from website.models import Video, Programme, Blog, Event, Link, Genre, QuestionsLive
from suit_redactor.widgets import RedactorWidget
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None,                {'fields': ['youtube_id','title','description', 'featured']}),
	    ('Categories',        {'fields': ['programmes', 'genre']}),
	]

class ProgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'featured','description']}),
    ]


class LinkInline(admin.StackedInline):
    model=Link

class PostForm(ModelForm):
    inlines = [
        LinkInline,
    ]

    class Meta:
        widgets = { 
            'detail': RedactorWidget(editor_options={'lang':'en'}),
            'summary': RedactorWidget(editor_options={'lang':'en'}),
            'date': SuitSplitDateTimeWidget,
            'start_date': SuitSplitDateTimeWidget,
            'end_date': SuitSplitDateTimeWidget,
        }

class BlogAdmin(admin.ModelAdmin):
    form=PostForm
    prepopulated_fields = {'slug': ('title',)}

class EventAdmin(admin.ModelAdmin):
    form=PostForm
    prepopulated_fields = {'slug': ('title',)}


class IQLResource(resources.ModelResource):

    class Meta:
        model = QuestionsLive


class IQLAdmin(ImportExportModelAdmin):
    readonly_fields = ('email', 'name', 'question', 'be_there', 'ip', 'user_agent', 'created_stamp')
    resource_class = IQLResource



admin.site.register(Link)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Programme, ProgAdmin)    
admin.site.register(Genre)
admin.site.register(QuestionsLive, IQLAdmin)
