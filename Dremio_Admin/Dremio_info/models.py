from django.db import models

# Create your models here.


class Source(models.Model):
    source_id = models.CharField(max_length=100)
    source_name = models.CharField(max_length=255)
    source_type = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name

class PhysicalDataSet(models.Model):
    physical_data_set_id = models.CharField(max_length=100)
    pds_path = models.CharField(max_length=255)
    pds_source = models.ForeignKey(Source, related_name='datasets', on_delete=models.CASCADE)

    def __str__(self):
        return self.pds_path