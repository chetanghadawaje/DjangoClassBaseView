from django.db import models


class customerModal(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=25, blank=True, null=True)
