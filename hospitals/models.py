from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

class Hospital(models.Model):
    name = models.CharField(_("Hospital Name"), max_length=200)
    lon = models.FloatField(_("Longitude"))
    lat = models.FloatField(_("Latitude"))
    fid = models.IntegerField(_("Field ID"))
    beds = models.IntegerField(_("Number of Beds"), default=1)
    province_name = models.CharField(_("Province"), max_length=100)
    province_code = models.CharField(_("Province Code"), max_length=1)
    geometry_field = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
    

