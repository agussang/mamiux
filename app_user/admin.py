from django.contrib import admin
from app_user.models import Tester


class UserAdmin(admin.ModelAdmin):

    """
    User in Admin
    """
    
    model = Tester
    list_display = [
        'user',
        'tester_name',
        'tester_email',
    ]

admin.site.register(Tester, UserAdmin)
