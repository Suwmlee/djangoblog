#coding=utf-8
from django.db import models
from django.contrib import admin
#from tinymce.widgets import TinyMCE
#from tinymce.models import HTMLField
from tinymce import models as tinymce_models
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    #body = models.TextField()
    #body  = HTMLField()
    body  = tinymce_models.HTMLField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = (
        '/static/tiny_mce/tiny_mce.js',
        '/static/tiny_mce/textarea.js',
        )
    list_display = ('title', 'timestamp')
    #formfield_overrides = {
        #models.TextField: {"widget": TinyMCE },
    #}


admin.site.register(BlogPost, BlogPostAdmin)
