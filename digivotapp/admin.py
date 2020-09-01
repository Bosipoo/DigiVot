from django.contrib import admin

# Register your models here.
from .models import State, Region
from .models import ElectionType
# from .models import Super_Registeradmin


class Statead(admin.ModelAdmin):
    list_display = ('id','name')
    list_per_page = 36

# class Districtad(admin.ModelAdmin):
#     list_display = ('id','state','district_name')
#     list_per_page = 36

class Regionad(admin.ModelAdmin):
    list_display = ('id','state','name')
    list_editable = ('name',)
    list_per_page = 36

# class Super(admin.ModelAdmin):
#     list_display = ('firstname','lastname','pin')
#     #list_editable = ('firstname','lastname',)
#     list_per_page = 10 
#     search_fields = ('firstname',)


@admin.register(ElectionType)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ['electionID', 'electiontitle', 'electiontype', 'voting_start', 'voting_end']


admin.site.register(State, Statead)
# admin.site.register(District, Districtad)
admin.site.register(Region, Regionad)
