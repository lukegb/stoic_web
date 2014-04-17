from django.contrib import admin
from django.forms import ModelForm
from posts.models import  Event, Link, Blog
from suit_redactor.widgets import RedactorWidget
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget

class LinkInline(admin.StackedInline):
    model=Link

class PostForm(ModelForm):
    inlines = [
        LinkInline,
    ]

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

admin.site.register(Link)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Event, EventAdmin)
