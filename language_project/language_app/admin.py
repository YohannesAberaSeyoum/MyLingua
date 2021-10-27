from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import	CustomUser,Preference,Course,Content,Quiz,Certificate,Grade

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['first_name','last_name','email','username','is_staff',]

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Preference)
admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Quiz)
admin.site.register(Certificate)
admin.site.register(Grade)