from django.contrib import admin
from django.contrib.admin import AdminSite #for changing the admid side css
from Admission_Form.models import Admission
class admssion(admin.ModelAdmin):
    list_display = ('full_name','photo')
admin.site.register(Admission,admssion)

admin.site.site_header = "SM Academy Admin Panel"
admin.site.site_title = "SM Academy Admin"
admin.site.index_title = "Welcome to SM Academy Dashboard"

# Register your models here.
