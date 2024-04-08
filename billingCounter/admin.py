from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from . models import Bill, OrderedProduct

class OrderedProductInline(admin.StackedInline):
    model = OrderedProduct

class BillAdmin(admin.ModelAdmin):
    inlines = [OrderedProductInline]

admin.site.register(Bill, BillAdmin)

# Register your models here.
def autoregister(*app_list):
    models = apps.get_models()
    for model in models:
        try:
            admin.site.register(model)
        except AlreadyRegistered:
            pass

autoregister("myapp")