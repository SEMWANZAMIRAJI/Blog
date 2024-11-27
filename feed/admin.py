from django.contrib import admin
from .models import Feed, User,Comment
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# class UserAdmin(UserAdmin):
#     model = User
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number', 'image')}),
#     )
    
    

# admin.site.unregister(User)

admin.site.register(User)
admin.site.register(Feed)
admin.site.register(Comment)
