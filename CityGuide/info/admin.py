from django.contrib import admin
from info.models import Categories, GcmTable, Pois, Preference, Region, SqliteSequence, UserT

# Register your models here.
class PoisAdmin(admin.ModelAdmin):
	list_display = ('name', 'intro')

admin.site.register(Pois, PoisAdmin)
admin.site.register(Categories)
admin.site.register(GcmTable)
admin.site.register(Preference)
admin.site.register(Region)
admin.site.register(SqliteSequence)
admin.site.register(UserT)