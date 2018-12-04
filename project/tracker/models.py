# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DeleteUrl(models.Model):
    url = models.CharField(primary_key=True, max_length=1000)
    modidate = models.DateField()

    class Meta:
        managed = False
        db_table = 'delete_url'
        unique_together = (('url', 'modidate'),)


class NewUrl(models.Model):
    url = models.CharField(primary_key=True, max_length=1000)
    modidate = models.DateField()

    class Meta:
        managed = False
        db_table = 'new_url'
        unique_together = (('url', 'modidate'),)


class Sitemap(models.Model):
    url = models.CharField(primary_key=True, max_length=1000)
    modidate = models.DateField()

    class Meta:
        managed = False
        db_table = 'sitemap'
