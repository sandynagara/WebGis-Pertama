from django.db import models
from django.contrib.gis.db import models as gismodels
# Create your models here.
class BangunanPogung(models.Model):
    nama = gismodels.CharField(max_length=254)
    jenis = gismodels.CharField(max_length=254)
    geom = gismodels.MultiPolygonField(srid=4326)