# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.cname


class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140, blank=True, null=True)
    diseasetype = models.ForeignKey('Diseasetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'

    def __str__(self):
        return self.disease_code

class Diseasetype(models.Model):
    diseasetype_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'

    def __str__(self):
        return f'{self.diseasetype_id}'

class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    doctor_degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return f'{self.email}'

class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'publicservant'

    def __str__(self):
        return f'{self.email}'

class Record(models.Model):
    email = models.OneToOneField(Publicservant, models.DO_NOTHING, db_column='email')
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        constraints = [
            models.UniqueConstraint(fields=['email', 'cname', 'disease_code'], name='unique_constraint_record')
        ]

class Specialize(models.Model):
    diseasetype = models.OneToOneField(Diseasetype, models.DO_NOTHING, db_index=True)
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email', db_index=True)

    class Meta:
        managed = False
        db_table = 'specialize'
        constraints = [
            models.UniqueConstraint(fields=['diseasetype', 'email'], name='unique_constraint_specialize')
        ]


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.email + f"({self.surname} {self.firstname})"