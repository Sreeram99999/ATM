from django.contrib import admin
from .models import Gender,Register,Acc_type,History

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    ...

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    ...

@admin.register(Acc_type)
class AccAdmin(admin.ModelAdmin):
    ...

admin.site.register(History)