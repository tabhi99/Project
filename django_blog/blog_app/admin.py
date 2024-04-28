from django.contrib import admin
from.models import BlogPost
from django.contrib.auth.models import Group
admin.site.site_header="Abhinav Blogging application"
admin.site.site_title = "Abhinav"
from django.utils.html import format_html

# Register your models here.
#admin.site.register(BlogPost)
admin.site.unregister(Group)


class CustomAdminPost(admin.ModelAdmin):
    list_display = ('Title','Publish_Date','Blog_Content','blog_content')
    date_hierarchy = 'Publish_Date'
    empty_value_display='NA'
    list_filter = ('Author','Publish_Date')
    search_fields =['Author']
    list_per_page = 4
    list_display_links = ['Blog_Content']
    list_editable = ['Publish_Date']


    def blog_content(self,obj):
        return format_html(f'<span style="color:red;">{obj.Blog_Content[:31]}</span>')


admin.site.register(BlogPost,CustomAdminPost)




