from django.contrib import admin
from .models import Place,Myrating


# Register your models here.
class MyratingAdmin(admin.ModelAdmin):
    model =Myrating
    list_display= ('place','rating','user')
    list_filter = ['place','user']
    search_fields = ['rating']
admin.site.register(Place)
admin.site.register(Myrating,MyratingAdmin)