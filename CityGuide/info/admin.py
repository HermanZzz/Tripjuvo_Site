from django.contrib import admin
from info.models import Categories, Pois, Preference, Region, UserT

# Register your models here.
class PoisAdmin(admin.ModelAdmin):
	list_display = ('name', 'intro')

class CateGoriesAdmin(admin.ModelAdmin) :
	list_display = ('name', 'image', 'marker')
	
class RegionAdmin(admin.ModelAdmin):
	list_display = ('city', 'latitude', 'longitude', 'picture')
	
class UserTAdmin(admin.ModelAdmin):
	list_display = ('ps', 'age', 'gender', 'p_vehicle')
		
		

admin.site.register(Pois, PoisAdmin)
admin.site.register(Categories, CateGoriesAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(UserT, UserTAdmin)