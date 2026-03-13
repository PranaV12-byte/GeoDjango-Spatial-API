from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Boundary

boundary_mapping = {
    "adm0_en": "ADM0_EN",
    "adm0_pcode": "ADM0_PCODE",
    "name": "ADM1_EN",
    "pcode": "ADM1_PCODE",
    "mpoly": "MULTIPOLYGON",
}

boundary_shp = Path(__file__).resolve().parent / "data" / "Boundary.shp"


def run(verbose=True):
    layer_mapping = LayerMapping(
        Boundary, str(boundary_shp), boundary_mapping, transform=False
    )
    layer_mapping.save(strict=True, verbose=verbose)
