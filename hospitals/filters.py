from boundaries.models import Boundary
from django_filters import rest_framework as filters
from rest_framework_gis.filters import GeoFilterSet
from .models import Hospital


class HospitalsFilter(GeoFilterSet):
    province = filters.CharFilter(
        method="get_hospitals_by_province", lookup_expr="within"
    )

    class Meta:
        model = Hospital
        exclude = ["geometry_field"]

    def get_hospitals_by_province(self, queryset, name, value):
        if value:
            try:
                boundary = Boundary.objects.get(pk=value)
                return queryset.filter(geometry_field__within=boundary.mpoly)
            except Boundary.DoesNotExist:
                return queryset.none()
        return queryset
