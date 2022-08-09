from django.contrib import admin
from .models import Account, Report, Building, Room, ReportType

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Account._meta.fields]
admin.site.register(Account, AccountAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Report._meta.fields]
admin.site.register(Report, ReportAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Room._meta.fields]
admin.site.register(Room, RoomAdmin)

class ReportTypeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReportType._meta.fields]
admin.site.register(ReportType, ReportTypeAdmin)

class BuildingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Building._meta.fields]
admin.site.register(Building, BuildingAdmin)