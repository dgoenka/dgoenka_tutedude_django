from django.contrib import admin

from accounts.models import Contact, Post


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)