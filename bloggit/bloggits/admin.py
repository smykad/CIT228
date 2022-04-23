from django.contrib import admin

from .models import Bloggit
from .models import Entry

# Register your models here.
admin.site.register(Bloggit)
admin.site.register(Entry)