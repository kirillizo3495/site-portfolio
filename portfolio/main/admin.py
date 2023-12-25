from django.contrib import admin
from .models import Post, Contact, Work


admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Work)

# Register your models here.
