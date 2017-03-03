import json

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import MultiPolygon

from .models import TaskConflict, TaskElement, Task, Participant


# Register your models here.
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_filter = ['experienced']
    search_fields = ['age']


@admin.register(TaskElement)
class ElementTaskAdmin(OSMGeoAdmin):
    def save_model(self, request, obj, form, change):
        """
        Override this so we can create the geometry when saving through the admin.
        """
        if obj.json:
            obj.element_geom = get_geom(json.dumps(obj.json))
            obj.json = {}
        obj.save()


@admin.register(TaskConflict)
class ConflictTaskAdmin(OSMGeoAdmin):
    def save_model(self, request, obj, form, change):
        """
        Override this so we can create the geometry when saving through the admin.
        """
        if obj.json:
            obj.conflict_geom = get_geom(json.dumps(obj.json))
            obj.json = {}
        obj.save()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Adds a “Filter” sidebar that lets people filter the change list by the pub_date field
    list_filter = ['num_of_elements']
    search_fields = ['title']


def get_geom(input_json):
    geojson = input_json
    ds = DataSource(geojson)
    geom_obj = None
    if len(ds) == 1:
        geoms = ds[0].get_geoms(geos=True)
        geom = geoms[0]
        # for geom in geoms:
        geom_type = geom.geom_type
        if geom_type == 'Polygon':
            geom_obj = MultiPolygon(geom)
        elif geom_type == 'Multipolygon':
            geom_obj = MultiPolygon(geom)
    return geom_obj
