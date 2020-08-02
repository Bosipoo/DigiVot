from django.contrib import admin

# Register your models here.
# from .models import AdminUserR
from .models import ManagerUserR
# from .models import Super_Registeradmin
from .models import VoterReg


# class AdminUSR(admin.ModelAdmin):
#     list_display = ('firstname','othername','lastname','phonenumber','email','DOB','address','gender','status','states','region','pictures','finger1','finger2')
#     list_editable = ('phonenumber',)
#     list_per_page = 10
#     search_fields = ('firstname','gender','email','lastname','phonenumber')
#     list_filter = ('gender',)

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
    list_display = ('firstname','othername','lastname','phonenumber','email','DOB','address','title','status','statesoforigin','statesofresidence','pictures','pin')
    list_editable = ('phonenumber',)
    list_per_page = 10
    search_fields = ('firstname','email','lastname','phonenumber')
    list_filter = ('title',)

# admin.site.register(AdminUserR, AdminUSR)
# admin.site.register(Super_Registeradmin, Super)
admin.site.register(VoterReg, voterUSR)
admin.site.register(ManagerUserR, ManagerUser)