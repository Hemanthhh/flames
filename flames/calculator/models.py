from django.db import models

class Data(models.Model):
    your_name = models.CharField(max_length = 100)
    partner_name = models.CharField(max_length = 100)
    