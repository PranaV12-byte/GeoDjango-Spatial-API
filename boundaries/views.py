from rest_framework import viewsets
from django.contrib.gis.db.models.functions import Area
from .models import Boundary
from .serializers import BoundarySerializer


class BoundaryViewsets(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer

    def get_queryset(self):
        boundary_area = Boundary.objects.annotate(area=Area("mpoly")).order_by("area")
        return boundary_area
