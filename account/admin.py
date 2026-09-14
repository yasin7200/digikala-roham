from django.contrib import admin

from .models import User, UserProfile

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")
    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)