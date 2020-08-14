from django.contrib import admin

# Register your models here.
from .models import AdminUserR,State, Region, District
from .models import ManagerUserR
# from .models import Super_Registeradmin
from .models import VoterReg


# class AdminUSR(admin.ModelAdmin):
#     list_display = ('firstname','othername','lastname','phonenumber','email','DOB','address','gender','status','states','region','pictures','finger1','finger2')
#     list_editable = ('phonenumber',)
#     list_per_page = 10
#     search_fields = ('firstname','gender','email','lastname','phonenumber')
#     list_filter = ('gender',)

class Statead(admin.ModelAdmin):
    list_display = ('id','name')
    list_per_page = 36

class Districtad(admin.ModelAdmin):
    list_display = ('id','state','district_name')
    list_per_page = 36

class Regionad(admin.ModelAdmin):
    list_display = ('id','state','name')
    list_editable = ('name',)
    list_per_page = 36

class ManagerUser(admin.ModelAdmin):
    list_display = ('firstname','othername','lastname','phonenumber','email','DOB','address','gender','pictures','pin')
    list_editable = ('phonenumber',)
    list_per_page = 10
    search_fields = ('firstname','gender','email','lastname','phonenumber')
    list_filter = ('gender',)

# class Super(admin.ModelAdmin):
#     list_display = ('firstname','lastname','pin')
#     #list_editable = ('firstname','lastname',)
#     list_per_page = 10 
#     search_fields = ('firstname',)

class voterUSR(admin.ModelAdmin):
    list_display = ('firstname','othername','lastname','phonenumber','email','DOB','address','title','status','state','statesofresidence','pictures','pin')
    list_editable = ('phonenumber',)
    list_per_page = 10
    search_fields = ('firstname','email','lastname','phonenumber')
    list_filter = ('title',)

admin.site.register(State, Statead)
admin.site.register(District, Districtad)
admin.site.register(Region, Regionad)
# admin.site.register(Super_Registeradmin, Super)
admin.site.register(VoterReg, voterUSR)
admin.site.register(ManagerUserR, ManagerUser)