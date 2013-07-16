from django.db import models
from django.contrib import admin
# Create your models here.
class linking(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    #timestamp = models.DateTimeField()


class linkingAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    #formfield_overrides = {
        #models.TextField: {"widget": TinyMCE },
    #}


admin.site.register(linking, linkingAdmin)
