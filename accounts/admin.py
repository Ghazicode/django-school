from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = models.User
        fields = ('national_code',)





class CustomUserAdmin(UserAdmin):
    model = models.User
    add_form = CustomUserCreationForm
    list_display = ('national_code', 'is_superuser', 'is_teacher', 'is_active', 'created_date')
    list_filter = ('national_code', 'is_superuser', 'is_active')
    searching_fields = ('national_code',)
    ordering = ('national_code', )
    fieldsets = (
        (None, {
            "fields":(
                'national_code',
                'password',
            ),
        }),
        ('permissions', {
            "fields":(
                'is_staff',
                'is_active',
                'is_superuser',
                'is_teacher',
                'is_student'
            ),
        }),
        ('group permissions', {
            "fields":(
                'groups',
                'user_permissions'
                
            ),
        }),
        ('important date', {
            "fields":(
                'last_login',
                
            ),
        }),
    )
    add_fieldsets=(
        (None, {
            'classes':(
                'wide',
            ),
            'fields':(
                'national_code',
                'password1',
                'password2',
                'is_superuser',
                'is_teacher',  
                'is_staff', 
                'is_active',
                'is_student,'
                
            ),
        }),
    )




class CustomUserProfile(admin.ModelAdmin):
    list_display = ('user', 'phone_number' , 'first_name', 'created_date')
    search_fields = ('user',)




admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Profile, CustomUserProfile)