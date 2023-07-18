from django.contrib import admin

from esl.models import CustomUser, VideoLecture

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name','email',  'user_type',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VideoLecture)