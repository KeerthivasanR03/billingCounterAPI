from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
def autoregister(*app_list):
    models = apps.get_models()
    for model in models:
        try:
            admin.site.register(model)
        except AlreadyRegistered:
            pass

autoregister("myapp")