from django.contrib import admin
from api.models import Company
from api.models import Vacancy
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'salary')