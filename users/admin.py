from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

CustomUser = get_user_model()

class CustomAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]




admin.site.register(CustomUser, CustomAdmin)


