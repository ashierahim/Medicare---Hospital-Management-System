from django.contrib import admin
from .models import dept, Doctors, Booking

class DeptAdmin(admin.ModelAdmin):
    list_display = ('id', 'dept_name', 'dep_desc')
    search_fields = ('dept_name',)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_name', 'doc_spec', 'dept_name')
    search_fields = ('doc_name', 'doc_spec')
    list_filter = ('dept_name',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booked_on')
    search_fields = ('p_name', 'p_email', 'p_phone')
    list_filter = ('doc_name', 'booked_on')

admin.site.register(dept, DeptAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Booking, BookingAdmin)