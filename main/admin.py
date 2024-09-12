from django.contrib import admin
from main import models

# Register your models here.
admin.site.register(models.Staff)

admin.site.register(models.Shift)

admin.site.register(models.StaffAttendance)

admin.site.register(models.StaffShift)

admin.site.register(models.Position)


admin.site.register(models.Admins)