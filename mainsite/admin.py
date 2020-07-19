from django.contrib import admin
from .models import Vocab

# Register your models here.
class VocabAdmin(admin.ModelAdmin):

    list_display = ("spanish", "english", "chinese", "classes", "pub_date")

admin.site.register(Vocab, VocabAdmin)
