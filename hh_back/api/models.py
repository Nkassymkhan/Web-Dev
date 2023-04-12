from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    city = models.CharField(max_length=250)
    address = models.TextField()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }
    def __str__(self):
        return self.name + "-" + self.city


class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.to_json()
        }

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    depth = 1