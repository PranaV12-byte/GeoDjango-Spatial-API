# Django Geospatial API

A production-ready geospatial REST API built with **Django 5**, **GeoDjango**, **Django REST Framework (DRF)**, and **PostGIS**. This API serves geospatial data for hospitals and administrative boundaries, allowing for complex geometric operations such as proximity searches and area calculations. The project is dockerized for easy development and deployment, leveraging Nginx as a reverse proxy.

## 🚀 Features

- **Spatial Database**: Powered by PostGIS to store and query geometries (`MultiPolygonField`, `PointField`).
- **RESTful Endpoints**: Built with Django REST Framework and DRF-GIS to serve GeoJSON.
- **Custom Spatial Queries**:
  - Calculate polygon areas dynamically.
  - Locate the closest hospitals within a specific radius using coordinates.
  - Filter hospitals by geographical boundaries (Points-in-Polygon).
- **Containerized**: Fully Dockerized environment including Django, Nginx, and PostGIS.
- **Admin Dashboard**: Integrated with `django-leaflet` for map-based geometry management.

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Django 5.0, Django REST Framework
- **Geospatial**: GeoDjango, GDAL, GEOS, PROJ
- **Database**: PostgreSQL 12 with PostGIS extension
- **Server**: Nginx, Gunicorn/Django Dev Server
- **Infrastructure**: Docker & Docker Compose

## 📦 Getting Started

### Prerequisites
- Docker and Docker Compose installed on your system.

### 1. Clone the repository
```bash
git clone <repository_url>
cd django-geospatial-api/hospitals-src
```

### 2. Environment Variables
Create a `.env` file in the project root by copying the example:
```bash
cp .env.example .env
```
Ensure it contains the necessary database credentials:
```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost 127.0.0.1 api nginx web
POSTGRES_DBNAME=hospital
POSTGRES_USER=admin
POSTGRES_PASS=admin123456
PG_HOST=postgres-db
PG_PORT=5432
```

### 3. Build and Run Containers
```bash
docker-compose up --build -d
```
*This will spin up `api`, `postgres-db`, and `nginx` containers.*

### 4. Run Migrations
Generate the required tables (including PostGIS spatial tables):
```bash
docker-compose exec api python manage.py migrate
```

### 5. Load Shapefile Data
The project includes `.shp` files for Boundaries and Hospitals. Use the provided mapping scripts to populate your database:
```bash
docker-compose exec api python manage.py shell
```
Inside the python shell:
```python
from boundaries import load as b_load
from hospitals import load as h_load

b_load.run()
h_load.run()
exit()
```

### 6. Create Superuser (Optional)
To access the Django Admin map interface:
```bash
docker-compose exec api python manage.py createsuperuser
```

## 🗺️ API Endpoints

The API routes traffic through Nginx on port `8080`.

### Hospitals
- **List/Create**: `GET /api/v1/hospitals/`
- **Total Bed Capacity**: `GET /api/v1/hospitals/total_bed_capacity/`
- **Provincial Bed Capacity**: `GET /api/v1/hospitals/province_beds_capacity/`
- **Find Closest Hospitals (3km radius)**: 
  `GET /api/v1/hospitals/closest_hospitals/?lon=<longitude>&lat=<latitude>`
- **Filter by Province (Spatial Intersect)**: 
  `GET /api/v1/hospitals/?province=<boundary_id>`

### Boundaries
- **List/Create**: `GET /api/v1/boundaries/`
  *(Returns boundaries sorted by dynamically calculated geometrical area).*

## 🧪 Code Quality
The codebase follows `flake8` and `black` style guidelines.
To check formatting:
```bash
docker-compose exec api black --check --exclude=migrations .
docker-compose exec api flake8 .
```

---
*Developed for robust geospatial data management and querying.*
