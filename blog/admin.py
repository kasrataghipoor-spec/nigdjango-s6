from django.contrib import admin
from .models import Post,Coment
# Register your models here.

admin.site.register([Post,Coment])