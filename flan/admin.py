from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.
class FlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image_url', 'short_name', 'price', 'is_private']

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_email', 'customer_name', 'message']

admin.site.register(Flan, FlanAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
#registra en el panel adm para visualizarlo