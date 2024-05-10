from django.contrib import admin
from .models import Doctor,Products,Schedule,Deals
from django.contrib.auth.models import Group
from django.utils.html import format_html
admin.site.site_header="Sujeet Dubey's Employee Admin"
admin.site.site_title="Sujeet's Emp Admin App"
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Products)
admin.site.register(Schedule)
admin.site.register(Deals)