from django.contrib import admin
from traveller.models import Traveller, Comment


admin.site.register(Traveller)
admin.site.register(Comment)

# @admin.register(Traveller)
# class TravellerAdmin(admin.AdminSite):
#     pass

# Register your models here.
