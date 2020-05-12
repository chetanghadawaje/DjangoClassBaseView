from django.db import models
from classBaseApp.validators import phone_number_validators


class customerModal(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=25, blank=True, null=True, validators=[phone_number_validators])

    def __int__(self):
        return self.cust_name