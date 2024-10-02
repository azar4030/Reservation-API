from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin as BaseModelAdmin
from django.utils.translation import gettext as _
# Register your models here.


class UserModelAdmin(BaseModelAdmin):
    ordering = ['id']
    list_display = ['email', 'f_name','l_name']
    fieldsets = (
        (_('Login Information'), {'fields': ('email', 'password')}),
        (_('Personal Information'),{'fields':('f_name','l_name','phone_number','img','national_code')}),
        (_('Permissions Information'),{'fields':('is_active','is_staff','is_superuser')}),
        (_('Dates'),{'fields':('birth_date','last_login')})

    )


admin.site.register(User, UserModelAdmin)
admin.site.register(Patient)
admin.site.register(Clinic)
admin.site.register(ClinicDoctor)
admin.site.register(ClinicSpecialty)
admin.site.register(Specialty)
admin.site.register(BusinessHours)
admin.site.register(Appointment)
admin.site.register(Doctor)

