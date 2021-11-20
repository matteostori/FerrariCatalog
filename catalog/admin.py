from django.contrib import admin

# Register your models here.
from .models import Car, Pilot, CarImage

# admin.site.register(Car)
admin.site.register(Pilot)
admin.site.register(CarImage)

# Define the admin class
class CarImageInline(admin.TabularInline):
    model = CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'pilot', 'caryear', 'maxspeed')
    list_filter = ('color', 'maxspeed', 'caryear')
    
    fieldsets = (
        ('General', {
            'fields': ('name', 'pilot', 'caryear', 'color', 'order')
        }),
        ('Technical details', {
            'fields': ('maxspeed', 'hp', 'cylinders')
        }),
        ('Other', {
            'fields': ('description',)
        }),
    )
    
    inlines = [CarImageInline]
