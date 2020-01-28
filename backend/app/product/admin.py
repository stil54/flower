from django.contrib import admin
from .models import Flower, Bunch, BunchContent

admin.site.register(Flower)
admin.site.register(Bunch)
admin.site.register(BunchContent)
