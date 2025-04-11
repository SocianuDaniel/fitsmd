from django.contrib import admin
from .models import Owner, OwnerProfile,User

# Register your models here.

admin.site.register(Owner)
admin.site.register(OwnerProfile)
admin.site.register(User)
